import os
import subprocess
import readline
import devicons
from simple_term_menu import TerminalMenu

def rlinput(prompt, default_value=""):
    readline.set_startup_hook(lambda: readline.insert_text(default_value))
    user_input = input(f"{prompt}")
    readline.set_startup_hook()
    return user_input

def find_templates():
    try:
        completed_process = subprocess.run(['xdg-user-dir', 'TEMPLATES'], capture_output=True, text=True)
        if completed_process.returncode == 0:
            return completed_process.stdout.strip() + '/'
    except FileNotFoundError:
        pass
    return os.environ.get('HOME', '') + '/Templates/'

def devicon_handler(file_name):
    try:
        extension = os.path.splitext(file_name)[-1][1:]
        return devicons.file_node_extensions[extension]
    except KeyError:
        return "?"

def generate_menu(files, icons=False):
    # generates items
    menu_items = ['None']

    for file in files:
        if icons:
            menu_items.append(f"{devicon_handler(file)} {file}")
        else:
            menu_items.append(file)

    options = {
        "menu_entries": menu_items,
        "status_bar": f"Item will be created at: {os.path.expanduser(os.getcwd())}",
        }

    # returns the menu
    return TerminalMenu(**options).show()
