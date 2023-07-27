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
    if args.get('version'): chech_version()

    TEMPLATE_DIR = find_templates()
    TEMPLATE_FILES = os.listdir(TEMPLATE_DIR)
    SELECTED = None

    # INPUT HANDLING
    menu_entry_index = generate_menu(TEMPLATE_FILES, icons=args.get('icons', False))

    if menu_entry_index == None or menu_entry_index == 0:
        sys.exit()
    else:
        SELECTED = menu_entry_index - 1

    # FILE CREATION
    # renaming file
    newName = rlinput(f'[NeFT] Create file: ', TEMPLATE_FILES[SELECTED])

    # copying file
    if len(newName.strip()) > 0:
        copy(str(os.path.join(TEMPLATE_DIR, TEMPLATE_FILES[SELECTED])), str(os.getcwd()))
        os.rename(TEMPLATE_FILES[SELECTED], newName)

        # Optionally print verbose output
        if args.get('verbose', False):
            print(f"[NeFT] File '{newName}' created from template '{TEMPLATE_FILES[SELECTED]}'.")

    else:
        print("[NeFT] Invalid file name. Aborting.")

    return args.get('inf', False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='NeFT - New From Template - Create a file from pre-defined templates.')
    parser.add_argument('-i', '--icons', action='store_true', help='draw icons in the menu')
    parser.add_argument('-l', '--loop', action='store_true', help='enable loop mode')
    # Add more arguments as needed
    args = parser.parse_args()

    while main(vars(args)): pass
