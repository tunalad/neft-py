# Icons taken from eza's source code
# https://github.com/eza-community/eza/blob/cf0c57d7ad160f3b73462892609cc9185964b298/src/output/icons.rs


class Icons:
    AUDIO = ""
    BINARY = ""
    BOOK = ""
    CALENDAR = ""
    CLOCK = ""
    COMPRESSED = ""
    CONFIG = ""
    CSS3 = ""
    DATABASE = ""
    DIFF = ""
    DISK_IMAGE = ""
    DOCKER = ""
    DOCUMENT = ""
    DOWNLOAD = "󰇚"
    EMACS = ""
    ESLINT = ""
    FILE = ""
    FILE_OUTLINE = ""
    FOLDER = ""
    FOLDER_CONFIG = ""
    FOLDER_GIT = ""
    FOLDER_GITHUB = ""
    FOLDER_HIDDEN = "󱞞"
    FOLDER_KEY = "󰢬"
    FOLDER_NPM = ""
    FOLDER_OPEN = ""
    FONT = ""
    GIST_SECRET = ""
    GIT = ""
    GRADLE = ""
    GRUNT = ""
    GULP = ""
    HTML5 = ""
    IMAGE = ""
    INTELLIJ = ""
    JSON = ""
    KEY = ""
    KEYPASS = ""
    LANG_ASSEMBLY = ""
    LANG_C = ""
    LANG_CPP = ""
    LANG_CSHARP = "󰌛"
    LANG_D = ""
    LANG_ELIXIR = ""
    LANG_FSHARP = ""
    LANG_GO = ""
    LANG_GROOVY = ""
    LANG_HASKELL = ""
    LANG_JAVA = ""
    LANG_JAVASCRIPT = ""
    LANG_KOTLIN = ""
    LANG_OCAML = ""
    LANG_PERL = ""
    LANG_PHP = ""
    LANG_PYTHON = ""
    LANG_R = ""
    LANG_RUBY = ""
    LANG_RUBYRAILS = ""
    LANG_RUST = ""
    LANG_SASS = ""
    LANG_STYLUS = ""
    LANG_TEX = ""
    LANG_TYPESCRIPT = ""
    LANG_V = ""
    LIBRARY = ""
    LICENSE = ""
    LOCK = ""
    MAKE = ""
    MARKDOWN = ""
    MUSTACHE = ""
    NODEJS = ""
    NPM = ""
    OS_ANDROID = ""
    OS_APPLE = ""
    OS_LINUX = ""
    OS_WINDOWS = ""
    OS_WINDOWS_CMD = ""
    PLAYLIST = "󰲹"
    POWERSHELL = ""
    PRIVATE_KEY = "󰌆"
    PUBLIC_KEY = "󰷖"
    RAZOR = ""
    REACT = ""
    README = "󰂺"
    SHEET = ""
    SHELL = "󱆃"
    SHELL_CMD = ""
    SHIELD_CHECK = "󰕥"
    SHIELD_KEY = "󰯄"
    SHIELD_LOCK = "󰦝"
    SIGNED_FILE = "󱧃"
    SLIDE = ""
    SUBLIME = ""
    SUBTITLE = "󰨖"
    TERRAFORM = "󱁢"
    TEXT = ""
    TYPST = "𝐭"
    UNITY = ""
    VECTOR = "󰕙"
    VIDEO = ""
    VIM = ""
    WRENCH = ""
    XML = "󰗀"
    YAML = ""
    YARN = ""


# Mapping from lowercase file extension to icons
EXTENSION_ICONS = {
    "7z": Icons.COMPRESSED,  # 
    "a": Icons.OS_LINUX,  # 
    "acc": Icons.AUDIO,  # 
    "acf": "",
    "ai": "",
    "aif": Icons.AUDIO,  # 
    "aifc": Icons.AUDIO,  # 
    "aiff": Icons.AUDIO,  # 
    "alac": Icons.AUDIO,  # 
    "android": Icons.OS_ANDROID,  # 
    "ape": Icons.AUDIO,  # 
    "apk": Icons.OS_ANDROID,  # 
    "apple": Icons.OS_APPLE,  # 
    "ar": Icons.COMPRESSED,  # 
    "arj": Icons.COMPRESSED,  # 
    "arw": Icons.IMAGE,  # 
    "asc": Icons.SHIELD_LOCK,  # 󰦝
    "asm": Icons.LANG_ASSEMBLY,  # 
    "asp": "",
    "avi": Icons.VIDEO,  # 
    "avif": Icons.IMAGE,  # 
    "avro": Icons.JSON,  # 
    "awk": Icons.SHELL_CMD,  # 
    "bash": Icons.SHELL_CMD,  # 
    "bat": Icons.OS_WINDOWS_CMD,  # 
    "bats": Icons.SHELL_CMD,  # 
    "bdf": Icons.FONT,  # 
    "bib": Icons.LANG_TEX,  # 
    "bin": Icons.BINARY,  # 
    "bmp": Icons.IMAGE,  # 
    "br": Icons.COMPRESSED,  # 
    "bst": Icons.LANG_TEX,  # 
    "bundle": Icons.OS_APPLE,  # 
    "bz": Icons.COMPRESSED,  # 
    "bz2": Icons.COMPRESSED,  # 
    "bz3": Icons.COMPRESSED,  # 
    "c": Icons.LANG_C,  # 
    "c++": Icons.LANG_CPP,  # 
    "cab": Icons.OS_WINDOWS,  # 
    "cbr": Icons.IMAGE,  # 
    "cbz": Icons.IMAGE,  # 
    "cc": Icons.LANG_CPP,  # 
    "cert": Icons.GIST_SECRET,  # 
    "cfg": Icons.CONFIG,  # 
    "cjs": Icons.LANG_JAVASCRIPT,  # 
    "class": Icons.LANG_JAVA,  # 
    "clj": "",
    "cljs": "",
    "cls": Icons.LANG_TEX,  # 
    "cmake": Icons.MAKE,  # 
    "cmd": Icons.OS_WINDOWS,  # 
    "coffee": "",
    "com": Icons.OS_WINDOWS_CMD,  # 
    "conf": Icons.CONFIG,  # 
    "config": Icons.CONFIG,  # 
    "cp": Icons.LANG_CPP,  # 
    "cpio": Icons.COMPRESSED,  # 
    "cpp": Icons.LANG_CPP,  # 
    "cr": "",
    "cr2": Icons.IMAGE,  # 
    "crdownload": Icons.DOWNLOAD,  # 󰇚
    "crt": Icons.GIST_SECRET,  # 
    "cs": Icons.LANG_CSHARP,  # 󰌛
    "csh": Icons.SHELL_CMD,  # 
    "cshtml": Icons.RAZOR,  # 
    "csproj": Icons.LANG_CSHARP,  # 󰌛
    "css": Icons.CSS3,  # 
    "csv": Icons.SHEET,  # 
    "csx": Icons.LANG_CSHARP,  # 󰌛
    "cts": Icons.LANG_TYPESCRIPT,  # 
    "cu": "",
    "cue": Icons.PLAYLIST,  # 󰲹
    "cxx": Icons.LANG_CPP,  # 
    "d": Icons.LANG_D,  # 
    "dart": "",
    "db": Icons.DATABASE,  # 
    "deb": "",
    "desktop": "",
    "di": Icons.LANG_D,  # 
    "diff": Icons.DIFF,  # 
    "djv": Icons.DOCUMENT,  # 
    "djvu": Icons.DOCUMENT,  # 
    "dll": Icons.LIBRARY,  # 
    "dmg": Icons.DISK_IMAGE,  # 
    "doc": Icons.DOCUMENT,  # 
    "docx": Icons.DOCUMENT,  # 
    "dot": "󱁉",
    "download": Icons.DOWNLOAD,  # 󰇚
    "drawio": "",
    "dump": Icons.DATABASE,  # 
    "dvi": Icons.IMAGE,  # 
    "dylib": Icons.OS_APPLE,  # 
    "ebook": Icons.BOOK,  # 
    "ebuild": "",
    "editorconfig": Icons.CONFIG,  # 
    "ejs": "",
    "el": Icons.EMACS,  # 
    "elc": Icons.EMACS,  # 
    "elm": "",
    "eml": "",
    "env": "",
    "eot": Icons.FONT,  # 
    "eps": Icons.VECTOR,  # 󰕙
    "epub": Icons.BOOK,  # 
    "erb": Icons.LANG_RUBYRAILS,  # 
    "erl": "",
    "ex": Icons.LANG_ELIXIR,  # 
    "exe": Icons.OS_WINDOWS_CMD,  # 
    "exs": Icons.LANG_ELIXIR,  # 
    "fdmdownload": Icons.DOWNLOAD,  # 󰇚
    "fish": Icons.SHELL_CMD,  # 
    "flac": Icons.AUDIO,  # 
    "flv": Icons.VIDEO,  # 
    "fnt": Icons.FONT,  # 
    "fon": Icons.FONT,  # 
    "font": Icons.FONT,  # 
    "fs": Icons.LANG_FSHARP,  # 
    "fsi": Icons.LANG_FSHARP,  # 
    "fsx": Icons.LANG_FSHARP,  # 
    "gdoc": Icons.DOCUMENT,  # 
    "gem": Icons.LANG_RUBY,  # 
    "gemfile": Icons.LANG_RUBY,  # 
    "gemspec": Icons.LANG_RUBY,  # 
    "gform": "",
    "gif": Icons.IMAGE,  # 
    "git": Icons.GIT,  # 
    "go": Icons.LANG_GO,  # 
    "gpg": Icons.SHIELD_LOCK,  # 󰦝
    "gradle": Icons.GRADLE,  # 
    "groovy": Icons.LANG_GROOVY,  # 
    "gsheet": Icons.SHEET,  # 
    "gslides": Icons.SLIDE,  # 
    "guardfile": Icons.LANG_RUBY,  # 
    "gv": "󱁉",
    "gvy": Icons.LANG_GROOVY,  # 
    "gz": Icons.COMPRESSED,  # 
    "h": Icons.LANG_C,  # 
    "h++": Icons.LANG_CPP,  # 
    "h264": Icons.VIDEO,  # 
    "haml": "",
    "hbs": Icons.MUSTACHE,  # 
    "heic": Icons.IMAGE,  # 
    "heics": Icons.VIDEO,  # 
    "heif": Icons.IMAGE,  # 
    "hpp": Icons.LANG_CPP,  # 
    "hs": Icons.LANG_HASKELL,  # 
    "htm": Icons.HTML5,  # 
    "html": Icons.HTML5,  # 
    "hxx": Icons.LANG_CPP,  # 
    "ical": Icons.CALENDAR,  # 
    "icalendar": Icons.CALENDAR,  # 
    "ico": Icons.IMAGE,  # 
    "ics": Icons.CALENDAR,  # 
    "ifb": Icons.CALENDAR,  # 
    "image": Icons.DISK_IMAGE,  # 
    "img": Icons.DISK_IMAGE,  # 
    "iml": Icons.INTELLIJ,  # 
    "inl": Icons.LANG_C,  # 
    "ini": Icons.CONFIG,  # 
    "ipynb": "",
    "iso": Icons.DISK_IMAGE,  # 
    "j2c": Icons.IMAGE,  # 
    "j2k": Icons.IMAGE,  # 
    "jad": Icons.LANG_JAVA,  # 
    "jar": Icons.LANG_JAVA,  # 
    "java": Icons.LANG_JAVA,  # 
    "jfi": Icons.IMAGE,  # 
    "jfif": Icons.IMAGE,  # 
    "jif": Icons.IMAGE,  # 
    "jl": "",
    "jmd": Icons.MARKDOWN,  # 
    "jp2": Icons.IMAGE,  # 
    "jpe": Icons.IMAGE,  # 
    "jpeg": Icons.IMAGE,  # 
    "jpf": Icons.IMAGE,  # 
    "jpg": Icons.IMAGE,  # 
    "jpx": Icons.IMAGE,  # 
    "js": Icons.LANG_JAVASCRIPT,  # 
    "json": Icons.JSON,  # 
    "jsx": Icons.REACT,  # 
    "jxl": Icons.IMAGE,  # 
    "kbx": Icons.SHIELD_KEY,  # 󰯄
    "kdb": Icons.KEYPASS,  # 
    "kdbx": Icons.KEYPASS,  # 
    "key": Icons.KEY,  # 
    "ko": Icons.OS_LINUX,  # 
    "ksh": Icons.SHELL_CMD,  # 
    "kt": Icons.LANG_KOTLIN,  # 
    "kts": Icons.LANG_KOTLIN,  # 
    "latex": Icons.LANG_TEX,  # 
    "ldb": Icons.DATABASE,  # 
    "less": "",
    "lhs": Icons.LANG_HASKELL,  # 
    "lib": Icons.LIBRARY,  # 
    "license": Icons.LICENSE,  # 
    "lisp": "󰅲",
    "localized": Icons.OS_APPLE,  # 
    "lock": Icons.LOCK,  # 
    "log": "",
    "ltx": Icons.LANG_TEX,  # 
    "lua": "",
    "lz": Icons.COMPRESSED,  # 
    "lz4": Icons.COMPRESSED,  # 
    "lzh": Icons.COMPRESSED,  # 
    "lzma": Icons.COMPRESSED,  # 
    "lzo": Icons.COMPRESSED,  # 
    "m": Icons.LANG_C,  # 
    "m2ts": Icons.VIDEO,  # 
    "m2v": Icons.VIDEO,  # 
    "m3u": Icons.PLAYLIST,  # 󰲹
    "m3u8": Icons.PLAYLIST,  # 󰲹
    "m4a": Icons.AUDIO,  # 
    "m4v": Icons.VIDEO,  # 
    "magnet": "",
    "markdown": Icons.MARKDOWN,  # 
    "md": Icons.MARKDOWN,  # 
    "md5": Icons.SHIELD_CHECK,  # 󰕥
    "mdb": Icons.DATABASE,  # 
    "mid": "󰣲",
    "mjs": Icons.LANG_JAVASCRIPT,  # 
    "mk": Icons.MAKE,  # 
    "mka": Icons.AUDIO,  # 
    "mkd": Icons.MARKDOWN,  # 
    "mkv": Icons.VIDEO,  # 
    "ml": Icons.LANG_OCAML,  # 
    "mli": Icons.LANG_OCAML,  # 
    "mll": Icons.LANG_OCAML,  # 
    "mly": Icons.LANG_OCAML,  # 
    "mm": Icons.LANG_CPP,  # 
    "mobi": Icons.BOOK,  # 
    "mov": Icons.VIDEO,  # 
    "mp2": Icons.AUDIO,  # 
    "mp3": Icons.AUDIO,  # 
    "mp4": Icons.VIDEO,  # 
    "mpeg": Icons.VIDEO,  # 
    "mpg": Icons.VIDEO,  # 
    "msi": Icons.OS_WINDOWS,  # 
    "mts": Icons.LANG_TYPESCRIPT,  # 
    "mustache": Icons.MUSTACHE,  # 
    "nef": Icons.IMAGE,  # 
    "ninja": "󰝴",
    "nix": "",
    "node": Icons.NODEJS,  # 
    "o": Icons.BINARY,  # 
    "odp": Icons.SLIDE,  # 
    "ods": Icons.SHEET,  # 
    "odt": Icons.DOCUMENT,  # 
    "ogg": Icons.AUDIO,  # 
    "ogm": Icons.VIDEO,  # 
    "ogv": Icons.VIDEO,  # 
    "opus": Icons.AUDIO,  # 
    "orf": Icons.IMAGE,  # 
    "org": "",
    "otf": Icons.FONT,  # 
    "out": "",
    "p12": Icons.KEY,  # 
    "par": Icons.COMPRESSED,  # 
    "part": Icons.DOWNLOAD,  # 󰇚
    "patch": Icons.DIFF,  # 
    "pbm": Icons.IMAGE,  # 
    "pcm": Icons.AUDIO,  # 
    "pdf": "",
    "pem": Icons.KEY,  # 
    "pfx": Icons.KEY,  # 
    "pgm": Icons.IMAGE,  # 
    "phar": Icons.LANG_PHP,  # 
    "php": Icons.LANG_PHP,  # 
    "pkg": "",
    "pl": Icons.LANG_PERL,  # 
    "plist": Icons.OS_APPLE,  # 
    "plx": Icons.LANG_PERL,  # 
    "pm": Icons.LANG_PERL,  # 
    "png": Icons.IMAGE,  # 
    "pnm": Icons.IMAGE,  # 
    "pod": Icons.LANG_PERL,  # 
    "pp": "",
    "ppm": Icons.IMAGE,  # 
    "pps": Icons.SLIDE,  # 
    "ppsx": Icons.SLIDE,  # 
    "ppt": Icons.SLIDE,  # 
    "pptx": Icons.SLIDE,  # 
    "properties": Icons.JSON,  # 
    "prql": Icons.DATABASE,  # 
    "ps": Icons.VECTOR,  # 󰕙
    "ps1": Icons.POWERSHELL,  # 
    "psd": "",
    "psd1": Icons.POWERSHELL,  # 
    "psf": Icons.FONT,  # 
    "psm1": Icons.POWERSHELL,  # 
    "pub": Icons.PUBLIC_KEY,  # 󰷖
    "purs": "",
    "pxm": Icons.IMAGE,  # 
    "py": Icons.LANG_PYTHON,  # 
    "pyc": Icons.LANG_PYTHON,  # 
    "pyd": Icons.LANG_PYTHON,  # 
    "pyi": Icons.LANG_PYTHON,  # 
    "pyo": Icons.LANG_PYTHON,  # 
    "qcow": Icons.DISK_IMAGE,  # 
    "qcow2": Icons.DISK_IMAGE,  # 
    "r": Icons.LANG_R,  # 
    "rar": Icons.COMPRESSED,  # 
    "raw": Icons.IMAGE,  # 
    "razor": Icons.RAZOR,  # 
    "rb": Icons.LANG_RUBY,  # 
    "rdata": Icons.LANG_R,  # 
    "rdb": "",
    "rdoc": Icons.MARKDOWN,  # 
    "rds": Icons.LANG_R,  # 
    "readme": Icons.README,  # 󰂺
    "rlib": Icons.LANG_RUST,  # 
    "rmd": Icons.MARKDOWN,  # 
    "rmeta": Icons.LANG_RUST,  # 
    "rpm": "",
    "rs": Icons.LANG_RUST,  # 
    "rspec": Icons.LANG_RUBY,  # 
    "rspec_parallel": Icons.LANG_RUBY,  # 
    "rspec_status": Icons.LANG_RUBY,  # 
    "rss": "",
    "rst": Icons.TEXT,  # 
    "rtf": Icons.TEXT,  # 
    "ru": Icons.LANG_RUBY,  # 
    "rubydoc": Icons.LANG_RUBYRAILS,  # 
    "s": Icons.LANG_ASSEMBLY,  # 
    "sass": Icons.LANG_SASS,  # 
    "sbt": Icons.SUBTITLE,  # 󰨖
    "scala": "",
    "scss": Icons.LANG_SASS,  # 
    "service": "",
    "sh": Icons.SHELL_CMD,  # 
    "sha1": Icons.SHIELD_CHECK,  # 󰕥
    "sha224": Icons.SHIELD_CHECK,  # 󰕥
    "sha256": Icons.SHIELD_CHECK,  # 󰕥
    "sha384": Icons.SHIELD_CHECK,  # 󰕥
    "sha512": Icons.SHIELD_CHECK,  # 󰕥
    "shell": Icons.SHELL_CMD,  # 
    "shtml": Icons.HTML5,  # 
    "sig": Icons.SIGNED_FILE,  # 󱧃
    "signature": Icons.SIGNED_FILE,  # 󱧃
    "slim": Icons.LANG_RUBYRAILS,  # 
    "sln": "",
    "so": Icons.OS_LINUX,  # 
    "sql": Icons.DATABASE,  # 
    "sqlite3": "",
    "srt": Icons.SUBTITLE,  # 󰨖
    "ssa": Icons.SUBTITLE,  # 󰨖
    "stl": Icons.IMAGE,  # 
    "sty": Icons.LANG_TEX,  # 
    "styl": Icons.LANG_STYLUS,  # 
    "stylus": Icons.LANG_STYLUS,  # 
    "sub": Icons.SUBTITLE,  # 󰨖
    "sublime-build": Icons.SUBLIME,  # 
    "sublime-keymap": Icons.SUBLIME,  # 
    "sublime-menu": Icons.SUBLIME,  # 
    "sublime-options": Icons.SUBLIME,  # 
    "sublime-package": Icons.SUBLIME,  # 
    "sublime-project": Icons.SUBLIME,  # 
    "sublime-session": Icons.SUBLIME,  # 
    "sublime-settings": Icons.SUBLIME,  # 
    "sublime-snippet": Icons.SUBLIME,  # 
    "sublime-theme": Icons.SUBLIME,  # 
    "svelte": "",
    "svg": Icons.VECTOR,  # 󰕙
    "swift": "",
    "t": Icons.LANG_PERL,  # 
    "tar": Icons.COMPRESSED,  # 
    "taz": Icons.COMPRESSED,  # 
    "tbz": Icons.COMPRESSED,  # 
    "tbz2": Icons.COMPRESSED,  # 
    "tc": Icons.DISK_IMAGE,  # 
    "tex": Icons.LANG_TEX,  # 
    "tf": Icons.TERRAFORM,  # 󱁢
    "tfstate": Icons.TERRAFORM,  # 󱁢
    "tfvars": Icons.TERRAFORM,  # 󱁢
    "tgz": Icons.COMPRESSED,  # 
    "tif": Icons.IMAGE,  # 
    "tiff": Icons.IMAGE,  # 
    "tlz": Icons.COMPRESSED,  # 
    "tml": Icons.CONFIG,  # 
    "toml": Icons.CONFIG,  # 
    "torrent": "",
    "ts": Icons.LANG_TYPESCRIPT,  # 
    "tsv": Icons.SHEET,  # 
    "tsx": Icons.REACT,  # 
    "ttc": Icons.FONT,  # 
    "ttf": Icons.FONT,  # 
    "twig": "",
    "txt": Icons.TEXT,  # 
    "typ": Icons.TYPST,  # 𝐭
    "txz": Icons.COMPRESSED,  # 
    "tz": Icons.COMPRESSED,  # 
    "tzo": Icons.COMPRESSED,  # 
    "unity": Icons.UNITY,  # 
    "unity3d": Icons.UNITY,  # 
    "v": Icons.LANG_V,  # 
    "vdi": Icons.DISK_IMAGE,  # 
    "vhd": Icons.DISK_IMAGE,  # 
    "video": Icons.VIDEO,  # 
    "vim": Icons.VIM,  # 
    "vmdk": Icons.DISK_IMAGE,  # 
    "vob": Icons.VIDEO,  # 
    "vue": "󰡄",
    "war": Icons.LANG_JAVA,  # 
    "wav": Icons.AUDIO,  # 
    "webm": Icons.VIDEO,  # 
    "webmanifest": Icons.JSON,  # 
    "webp": Icons.IMAGE,  # 
    "whl": Icons.LANG_PYTHON,  # 
    "windows": Icons.OS_WINDOWS,  # 
    "wma": Icons.AUDIO,  # 
    "wmv": Icons.VIDEO,  # 
    "woff": Icons.FONT,  # 
    "woff2": Icons.FONT,  # 
    "wv": Icons.AUDIO,  # 
    "xcf": Icons.IMAGE,  # 
    "xhtml": Icons.HTML5,  # 
    "xlr": Icons.SHEET,  # 
    "xls": Icons.SHEET,  # 
    "xlsm": Icons.SHEET,  # 
    "xlsx": Icons.SHEET,  # 
    "xml": Icons.XML,  # 󰗀
    "xpm": Icons.IMAGE,  # 
    "xul": Icons.XML,  # 󰗀
    "xz": Icons.COMPRESSED,  # 
    "yaml": Icons.YAML,  # 
    "yml": Icons.YAML,  # 
    "z": Icons.COMPRESSED,  # 
    "zig": "",
    "zip": Icons.COMPRESSED,  # 
    "zsh": Icons.SHELL_CMD,  # 
    "zsh-theme": Icons.SHELL,  # 󱆃
    "zst": Icons.COMPRESSED,  # 
}
