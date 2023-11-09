# NeFT - New From Template

NeFT is a simple command-line tool that allows you to create new files using pre-made templates.

I developed this tool during my transition to a more CLI based workflow when I found myself missing the convenience of the 'Create New' option in GUI file managers.

# Table of contents

1. [Usage](#1-usage)
2. [Configuration](#2-configuration)
3. [Dependencies](#3-dependencies)
4. [Install](#4-install)

# 1. Usage

```
NeFT - New From Template - Create files from pre-defined templates.

options:
  -h, --help            show this help message and exit
  -i, --icons           draw icons in the menu
  -l, --loop            enable loop mode
  -f, --full-path       draw the whole file path
  -xdg, --use-xdg-path  include xdg-user-dir templates path
  -c PATH, --config PATH
                        configuration file path
  -s SORT_TYPE, --sort SORT_TYPE
                        sort files by name or extension
  -r, --reverse         reverse the sorting order
  -o PATH, --output PATH
                        output path
```

# 2. Configuration

```yaml
# example config file
# none of these are required
# but "paths" are recommended

paths: # defining paths (not required if using use_xdg_path)
    - "~/Templates/"
    - "~/.local/share/templates/"

icons: true # draw icons
full_path: false # print the whole path
loop: false # loop mode
use_xdg_path: false # include xdg-user-dir templates path
sort: "name" # sort files by "name" or "extension"
reverse: true # reverse the sorting order
```

# 3. Dependencies

Pip packages that this tool uses aren't required to be installed; that will be handled during the build process inside a virtual environment.

-   `python`
-   `xdg-user-dirs` (required **only if** using the `-xdg` option)
-   `patchelf` (required for building the binary)

# 4. Install

Binary `neft` will be located at `~/.local/bin/`

```
git clone https://github.com/tunalad/neft-py.git
cd neft-py
make install
```
