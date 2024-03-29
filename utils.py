# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=unspecified-encoding
import os
from sys import exit
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


def generate_menu(files, icons=False, full_path=False, output=None):
    # generates items
    menu_items = ["None"]

    for file in files:
        if not full_path:
            file = os.path.basename(file)
            if icons:
                menu_items.append(f"{devicon_handler(file)} {file}")
            else:
                menu_items.append(file)
        else:
            if icons:
                menu_items.append(f"{devicon_handler(file)} {file}")
            else:
                menu_items.append(file)

    options = {
        "menu_entries": menu_items,
        "status_bar": f"Item will be created at: {os.path.expanduser(output or os.getcwd())}",
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
    if sort_by == "name":
        return sorted(files, key=lambda x: os.path.basename(x).lower(), reverse=reverse)
    if sort_by == "extension":
        return sorted(
            files, key=lambda x: os.path.splitext(x)[1].lower(), reverse=reverse
        )
    return files
