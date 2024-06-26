# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=unspecified-encoding
import os
from shutil import copy, move
import subprocess
import readline
import nerd_icons
import yaml
from simple_term_menu import TerminalMenu


def rlinput(prompt, default_value=""):
    readline.set_startup_hook(lambda: readline.insert_text(default_value))
    user_input = input(f"{prompt}")
    readline.set_startup_hook()
    return user_input


def normalize_path(path):
    if path.startswith("~"):
        return os.path.expanduser(path)
    if path.startswith("$"):
        return os.path.expandvars(path)
    return path


def templates_dict(files, icons=False, full_path=False):
    menu_items = {}

    for file in files:
        if not full_path:
            basename = os.path.basename(file)
            original_basename = basename

            if icons:
                basename = f"{devicon_handler(original_basename)} {basename}"
                original_basename = basename

            # handle multiple files with the same name
            count_duplicates = 1
            while basename in menu_items:
                basename = f"{original_basename} ({count_duplicates})"
                count_duplicates += 1

            menu_items[basename] = file
        else:
            if icons:
                menu_items[f"{devicon_handler(os.path.basename(file))} {file}"] = file
            else:
                menu_items[file] = file

    return menu_items


def find_templates(paths=[], use_xdg_path=False, sort_by="name", reverse=False):
    if use_xdg_path:
        try:
            completed_process = subprocess.run(
                ["xdg-user-dir", "TEMPLATES"],
                capture_output=True,
                text=True,
                check=True,
            )
            if completed_process.returncode == 0:
                paths.insert(0, completed_process.stdout.strip() + "/")
        except FileNotFoundError:
            print("[NeFT] Command xdg-user-dir not found. Ignoring the option.")

    # path normalizing
    normalized_paths = [normalize_path(path) for path in paths]
    templates = []

    # finding files
    for path in normalized_paths:
        files = os.listdir(path)
        templates.extend([os.path.join(path, file) for file in files])

    # removing directories
    templates = [path for path in templates if os.path.isfile(path)]

    return sort_files(templates, sort_by, reverse)


def devicon_handler(file_name):
    try:
        extension = os.path.splitext(file_name)[-1][1:]
        return nerd_icons.EXTENSION_ICONS[extension]
    except KeyError:
        return nerd_icons.Icons().FILE


def generate_menu(files, icons=False, full_path=False, multi_select=False):
    # generates items
    menu_items = {"None": "None"}
    menu_items.update(templates_dict(files, icons, full_path))

    def get_path(item):
        if item == "None":
            return "File path: "
        return menu_items[item]

    options = {
        "menu_entries": list(menu_items.keys()),
        "status_bar": get_path,
        "multi_select": multi_select,
        "multi_select_select_on_accept": False,
    }

    # returns the menu
    return TerminalMenu(**options).show()


def load_config(paths):
    for path in paths:
        if path is not None and os.path.exists(normalize_path(path)):
            with open(normalize_path(path), "r") as file:
                config = yaml.safe_load(file)
                return config
    return {}


def sort_files(files, sort_by, reverse):
    match sort_by:
        case "name":
            return sorted(
                files, key=lambda x: os.path.basename(x).lower(), reverse=reverse
            )
        case "extension":
            return sorted(
                files, key=lambda x: os.path.splitext(x)[1].lower(), reverse=reverse
            )
        case _:
            return files


# # # # # # # # # # # #
# # # SUBCOMMANDS # # #
# # # # # # # # # # # #


def add_template(file, template_dir):
    template_dir = normalize_path(template_dir)

    file_name, extension = os.path.splitext(os.path.basename(file))

    # if file with that name already exists, add index in the name
    if os.path.exists(os.path.join(template_dir, f"{file_name}{extension}")):
        index = 1
        while os.path.exists(
            os.path.join(template_dir, f"{file_name} ({index}){extension}")
        ):
            index += 1

        new_file_name = f"{file_name} ({index}){extension}"
    else:
        new_file_name = f"{file_name}{extension}"

    # copy the file w/ new name
    copy(file, os.path.join(template_dir, new_file_name))
    print(f"[NeFT] Added '{new_file_name}' to '{template_dir}'.")


def remove_template(files):
    for file in files:
        try:
            os.remove(file)
            print(f"[NeFT] Removed '{file}'.")
        except Exception as e:
            print(f"[NeFT] An error ocurred while removing '{file}':\n")


def rename_template(old_path, new_name):
    path, old_name = os.path.split(old_path)

    # Making sure path ends with a separator
    path = os.path.join(path, "")

    new_path = os.path.join(path, new_name)

    # Making sure the file exists at the old path
    if os.path.isfile(old_path):
        # Making sure the new path doesn't exist already
        if os.path.exists(new_path):
            print(f"[NeFT] '{new_path}' already exists. Skipping rename.")
            return

        # Renaming the file
        move(old_path, new_path)
        print(f"[NeFT] Renamed '{old_name}' to '{new_name}'.")
    else:
        print("[NeFT] Couldn't find the template.")


def list_templates(files, icons=False, full_path=False):
    menu_items = templates_dict(files, icons, full_path)

    for item in menu_items:
        print(item)
