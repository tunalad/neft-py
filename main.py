#!./venv/bin/python
# pylint: disable=consider-using-sys-exit

# NeFT - New From Template
# Create a file from pre-defined templates.

import argparse
from shutil import copy
import os
import sys
from utils import rlinput, find_templates, devicon_handler, generate_menu

def main(args):
    # FINDING TEMPLATES
    paths = ["~/.local/share/templates/"]
    TEMPLATE_FILES = find_templates(paths=paths, use_xdg_path=args.get("use_xdg_path", False))

    # INPUT HANDLING
    menu_entry_index = generate_menu(TEMPLATE_FILES, icons=args.get("icons", False), full_path=args.get("full_path", False), output=args.get('output', None))

    if menu_entry_index == None or menu_entry_index == 0:
        sys.exit()
    else:
        SELECTED = menu_entry_index - 1

    # FILE CREATION
    newName = ''
    if args.get('output'): 
        newName = args.get('output')
    else:
        newName = rlinput(f'[NeFT] Create file: ', os.path.basename(TEMPLATE_FILES[SELECTED]))

    if len(newName.strip()) > 0:
        # copying file
        copied_file = os.path.join(os.getcwd(), newName)
        copy(str(os.path.join(TEMPLATE_FILES[SELECTED])), copied_file)
    else:
        print("[NeFT] Invalid file name. Aborting.")

    return args.get('loop', False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NeFT - New From Template - Create a file from pre-defined templates.')
    parser.add_argument('-i', '--icons', action='store_true', help='draw icons in the menu')
    parser.add_argument('-l', '--loop', action='store_true', help='enable loop mode')
    parser.add_argument('-f', '--full-path', action='store_true', help='draw the whole file path')
    parser.add_argument('-o', '--output', metavar="PATH", type=str, help='output path')
    parser.add_argument('-xdg', '--use-xdg-path', action='store_true', help='include xdg-user-dir templates path')
    # Add more arguments as needed
    args = parser.parse_args()

    while main(vars(args)): pass
