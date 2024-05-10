#!./venv/bin/python
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=redefined-outer-name

# NeFT - New From Template
# Create files from pre-defined templates.

import argparse
from shutil import copy
import os
import sys
from argparse_formatter import ParagraphFormatter, FlexiFormatter
from utils import (
    rlinput,
    find_templates,
    generate_menu,
    load_config,
    add_template,
    remove_template,
    rename_template,
    list_templates,
)


def main(args):
    # FINDING TEMPLATES
    paths = config.get("paths", ["~/Templates"])
    try:
        template_files = find_templates(
            paths=paths,
            use_xdg_path=args.get("use_xdg_path", False),
            sort_by=args.get("sort", "name"),
            reverse=args.get("reverse", False),
        )
    except:
        sys.exit(
            "[NeFT] Couldn't find any template directories. Either create ~/Templates or define paths in neft.yaml."
        )

    # SUBCOMMANDS
    if args.get("subcommand_name"):
        try:
            subcmd = args.get("subcommand_name")
            match subcmd:
                case "add":
                    add_template(args.get("PATH"), paths[0])
                case "remove":
                    remove_template(args.get("TEMPLATE"), paths)
                case "rename":
                    rename_template(args.get("OLD"), args.get("NEW"), paths)
                case "list":
                    list_templates(
                        template_files,
                        icons=args.get("icons", False),
                        full_path=args.get("full_path", False),
                    )
            sys.exit()
        except (AttributeError, KeyError, FileNotFoundError):
            sys.exit("[NeFT] Invalid input.")

    # INPUT HANDLING
    menu_entry_index = generate_menu(
        template_files,
        icons=args.get("icons", False),
        full_path=args.get("full_path", False),
    )

    if menu_entry_index is None or menu_entry_index == 0:
        sys.exit()
    else:
        selected = menu_entry_index - 1

    # FILE CREATION
    new_name = ""
    if args.get("output"):
        new_name = args.get("output")
    else:
        new_name = rlinput(
            "[NeFT] Create file: ", os.path.basename(template_files[selected])
        )

    if len(new_name.strip()) > 0:
        # copying file
        copied_file = os.path.join(os.getcwd(), new_name)
        copy(str(os.path.join(template_files[selected])), copied_file)
    else:
        print("[NeFT] Invalid file name. Aborting.")

    return args.get("loop", False)


if __name__ == "__main__":
    # fmt: off
    parser = argparse.ArgumentParser(
        prog="neft",
        usage="%(prog)s [OPTION]... [SUBCOMMAND]... [FILE]...",
        description="NeFT - New From Template - Create files from pre-defined templates.",
    )

    parser.add_argument("-i", "--icons", action="store_true", help="draw icons in the menu")
    parser.add_argument("-l", "--loop", action="store_true", help="enable loop mode")
    parser.add_argument("-f", "--full-path", action="store_true", help="draw the whole file path")
    parser.add_argument("-xdg", "--use-xdg-path", action="store_true", help="include xdg-user-dir templates path",)
    parser.add_argument("-c", "--config", metavar="", type=str, help="configuration file path")
    parser.add_argument("-s", "--sort", metavar="", type=str, default="name", help="sort files by name or extension")
    parser.add_argument("-r", "--reverse", action="store_true", help="reverse the sorting order")
    parser.add_argument("-o", "--output", metavar="", type=str, help="output path")

    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand_name")
    subparsers.add_parser("list", help="list all templates")
    subparsers.add_parser("add", help="add file to templates").add_argument("PATH", help="path to the file to be added")
    subparsers.add_parser("remove", help="remove a template").add_argument("TEMPLATE", type=str, help="template name to be removed")

    rename_parser = subparsers.add_parser("rename", help="rename template")
    rename_parser.add_argument("OLD", help="old template name")
    rename_parser.add_argument("NEW", help="new template name")
    # fmt: on

    # add more arguments as needed
    args = parser.parse_args()

    # config overwriting
    config_path = [
        args.config,
        "$XDG_CONFIG_HOME/neft/neft.yaml",
        "$XDG_CONFIG_HOME/neft.yaml",
        "~/.config/neft/neft.yaml",
        "~/.config/neft.yaml",
        "~/.neft.yaml",
    ]

    # load config
    config = load_config(config_path)

    if config:
        for key, value in config.items():
            # propritize these passed options over the config one
            skipable_args = ["sort", "reverse", "use_xdg_path"]
            if key in skipable_args:
                continue

            # applying passed options
            if hasattr(args, key) and value:
                setattr(args, key, value)

    while main(vars(args)):
        pass
