# NeFT - New From Template

NeFT is a simple command-line tool that allows you to create new files using pre-made templates.

I developed this tool during my transition to a more CLI based workflow when I found myself missing the convenience of the 'Create New' option in GUI file managers.

## Usage

```
usage: main.py [-h] [-i] [-l] [-f] [-o PATH] [-xdg]

NeFT - New From Template - Create a file from pre-defined templates.

options:
  -h, --help            show this help message and exit
  -i, --icons           draw icons in the menu
  -l, --loop            enable loop mode
  -f, --full-path       draw the whole file path
  -o PATH, --output PATH
                        output path
  -xdg, --use-xdg-path  include xdg-user-dir templates path
```

## Install

Binary will be located at `~/.local/bin/`

```
git clone https://github.com/tunalad/neft-py.git
cd neft-py
make install
```

Pip packages that this tool uses aren't required to be installed; that will be handled during the build process inside a virtual environment.

## Dependencies

-   `python`
-   `xdg-user-dirs`.
