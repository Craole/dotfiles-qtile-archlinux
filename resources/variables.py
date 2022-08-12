#!/usr/bin/env python
# coding=utf-8
# VARIABLES


# ----------------------------
# ---------- Imports ---------
# ----------------------------

# >>= Standard ===#
import os
from datetime import datetime as dt

# >>= Third-Party ===#

# >>= Local ===#


# ----------------------------
# ------ Modifier Keys -------
# ----------------------------

alt = ['mod1']
sht = ['shift']
ctl = ['control']
supW = ['mod4']
supA = ['mod4', 'mod1']
supS = ['mod4', 'shift']
supC = ['mod4', 'control']
ctlS = ['control', 'shift']
altS = ['mod1', 'shift']
altC = ['mod1', 'control']
altSC = ['mod1', 'shift', 'control']
supSC = ['mod4', 'shift', 'control']
qUp = 'k'
qDown = 'l'
qLeft = 'h'
qRight = 'j'

# ----------------------------
# ----------- Paths ----------
# ----------------------------

home = os.path.expanduser('~/')
lbin = home + '.local/bin/cc/'
conf = home + '.config/'
dotfiles = home + 'Dotfiles/dotfiles.code-workspace'
dotfrommyfriends = home + \
    '/Downloads/Dotfiles/dotfiles.code-workspace'
screenshots = home + 'Pictures/Screenshots/'

# >>= DMenu =<< #
dconf = conf + 'dmenu/'
dmScripts = dconf + 'scripts/'

# >>= Qtile =<< #
qconf = conf + 'qtile/'
qIcons = qconf + 'icons/'
qThemes = qconf + 'themes/'
qImports = qconf + 'modules/'
qScripts = qconf + 'scripts/'
qKeys = qconf + 'utils/keys.py'
autostart = qScripts + 'autostartA.sh'
refresh = qScripts + 'autostartB.sh'
picom = qScripts + 'picom-toggle.sh'
wallpaper = qScripts + 'set-pywal.sh'

# >>= LBin =<< #
nm = lbin + 'network.sh'
nmShow = lbin + 'network.sh ShowInfo'

# ----------------------------
# ------- Applications -------
# ----------------------------


# >>= TERMINAL =<< #

Terminal = [
    'alacritty',
    'kitty',
    'st',
]
termRadio = [
    ' -e curseradio',
    ' -e curseradio-improved',
]
termUpdate = [
    ' -e paru'
    ' -e update'
]
termSys = [
    ' -e bpytop',
    ' gotop'
]
colorPicker = [
    Terminal[2] + ' -e colorpicker'
]
xprop = Terminal[2] + '-e xprop'
xev = Terminal[1] + '-e xv'
nmUI = Terminal[2] + ' -e nmtui'


# >>= BRIGHTNESS CONTROL =<< #

bclDown = [
    'sudo xbacklight -10',
    lbin + 'brightness down',
]
bclUp = [
    'sudo xbacklight +10',
    lbin + 'brightness up',
]


# >>= VOLUME CONTROL =<< #

volMute = [
    'amixer set Master toggle'
]
volDown = [
    'pulseaudio-ctl down 5',
    lbin + 'volume down',
    'amixer - c 0 - q set Master 2dB -',
]
volUp = [
    'pulseaudio-ctl up 5',
    lbin + 'volume up',
    'amixer - c 0 - q set Master 2dB +',
]


# >>= LAUNCHER =<< #

Launcher = [

    #=== jgMenu ===#
    'jgmenu_run',

    #=== Rofi ===#
    "rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \'Run: \' -drun-display-format \'{name}\'",

    #=== dMenu ===#
    "dmenu_run -p 'Run: '",
]

dMenu = [
    Launcher[2],
    dmScripts + './dmconf',
    dmScripts + './dmscrot',
    dmScripts + './dmkill',
    dmScripts + './dmlogout',
    dmScripts + './dman',
    dmScripts + './dmred',
    dmScripts + './dmsearch',
    'passmenu'


]
# >>= WEB BROWSER =<< #
Browser = [
    'brave-nightly',
    'firefox',
    'vivaldi-stable',
]

# >>= DEVELOPMENT =<< #
iDE = [
    'code',
    'emacsclient - c - a emacs',
]
VSCode = [
    iDE[0],
    iDE[0] + ' ' + dotfiles,
    iDE[0] + ' ' + dotfrommyfriends,
]
Emacs = [
    iDE[1],
    iDE[1] + "--eval '(ibuffer)'",
    iDE[1] + "--eval '(dired nil)'",
    iDE[1] + "--eval '(erc)'",
    iDE[1] + "--eval '(mu4e)'",
    iDE[1] + "--eval '(elfeed)'",
    iDE[1] + "--eval '(eshell)'",
    iDE[1] + "--eval '(+vterm/here nil)'",

]
Editor = [
    'sudo notepadqq --allow-root',
    'nvim',
    'vim'
    'sudo featherpad',
    'micro'
]


# >>= Sys Management =<< #
appManager = [
    'pamac-manager',
    Terminal[0] + termUpdate[0],
]
appKill = ['xkill']
sysViewer = [
    Terminal[0] + termSys[0],
    'htop'
]
sysManager = [
    'stacer',
    'Nm-connection-editor',
]
guiFM = [
    'pcmanfm-qt',
    'sudo doublecmd --no-splash',
    'doublecmd',
]
termFM = [
    'lf',
    'nnn',
    'ranger',
]
fontManager = [
    'com.github.fontmatrix.Fontmatrix --no-splash',
    'Font-Manager',
]
screenLock = [
    Terminal[2] + ' -e betterlockscreen -l blur',
    'i3lock -c 000000',
    'slock',
]

# >>= Media =<< #
musicPlayer = [
    'yarock',
    'deadbeef'
]
videoPlayer = [
    'mpv',
    'vlc',
]
radioPlayer = [
    'shortwave',
    Terminal[0] + termRadio[0],
    'MellowPlayer',
]
YouTube = [
    'gtk-pipe-viewer',
]
mediaPlayer = [
    musicPlayer[0],
    radioPlayer[0],
    videoPlayer[0],
]
Calculator = [
    'speedcrunch'
]
Downloader = [
    'qbittorrent'
]
eMail = [
    'thunderbird-nightly',
    'thunderbird',
    'trojita',
]

# ----------------------------
# --------- Colors -----------
# ----------------------------

colLight = [
    '#ECEDEC',
    '#CECECE',
    '#6d6e6f',  # Rasta
    '#7DD575',
]
colDark = [
    '#272727',  # Materia
    '#0e0c0b',  # Rasta
    '#36383E',  # Vimix
    '#1C1B22',
    '#3d3f4b',
    '#110015E0',
]
colAccent = [
    '#009c37',  # Jamaica
    '#fed200',  # Jamaica
    '#018a2d',  # Rasta
    '#a65a42',  # Rasta
    '#8800AA',  # Violet
]
colAlert = [
    '#FF0000'
    '#d51c2c',  # Rasta
    '#fcde03',  # Rasta
    '#FF6F00'
]

# ----------------------------
# ---------- Fonts -----------
# ----------------------------
fonts = [
    {
        'Icon': [
            'FiraCode Nerd Font',
            'Hack Nerd Font',
            'CaskaydiaCove Nerd Font'
            'HeavyData Nerd Font',
        ]
    },
    {
        'Display': [
            'Comfortaa Bold',
            'Rec Mono Casual',
            'Cascadia Code Bold',
        ],
    },
    {
        'Fancy': [
            'OpenDyslexic Nerd Font',
            'VictorMono Nerd Font Bold Italic',
        ]
    }
]
fontIcon = [
    'Hack Nerd Font',
    'HeavyData Nerd Font',
]
fontDisplay = [
    'Comfortaa Bold',
    'Rec Mono Casual',
    'Cascadia Code Bold',
]
fontFancy = [
    'OpenDyslexic Nerd Font',
    'VictorMono Nerd Font Bold Italic',
]

# ----------------------------
# ---------- Dates -----------
# ----------------------------


def suffix(d):
    # => Set rules for ordinal numbers in date (th, nd or st)
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def dateX(format, t):
    # => Generate date with ordinal numbers
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


def dateNow():
    # => Date format
    # return dateX('%a, {S} %B', dt.now())
    return dateX('%a, {S} %b  %H:%M', dt.now())


# ----------------------------
# -------- WORKSPACES --------
# ----------------------------


workspaces = [
    {
        'key': 'grave',
        'label': ' ',
        'name': 'TERM',
        'layout': 'monadwide',
        'wm_class': [
            # 'alacritty',
            'kitty',
            # 'st',
        ],
        'wm_name':[],
    },
    {
        'key': '1',
        'label': ' ₁',
        'name': 'CODE',
        'layout': 'monadwide',
        'wm_class': [
            'Code',
            'Code-oss',
        ],
        'wm_name':[],
    },
    {
        'key': '2',
        'label': ' ₂',
        'name': 'WWW',
        'layout': 'monadwide',
        'wm_class': [
            # 'firefox',
            'qutebrowser'
            'brave-browser',
            'Brave-browser-nightly',
            'chromium',
            'google-chrome',
        ],
        'wm_name':[],
    },
    {
        'key': '3',
        'label': ' ₃',
        'name': 'TOOL',
        'layout': 'monadtall',
        'wm_class': [
            'fontmatrix',
            'Font-manager',
            'pcmanfm-qt',
            'Double Commander',
            'Pamac-manager',
            'stacer',
        ],
        'wm_name':[
            '*Double Commander*',
        ],
    },
    {
        'key': '4',
        'label': '  ₄',
        'name': 'MAIL',
        'layout': 'monadtall',
        'wm_class': [
            'thunderbird',
            'Daily',
            'evolution',
            'geary',
            'mail',
        ],
        'wm_name':[],
    },
    {
        'key': '5',
        'label':  '行  ₅',
        'name': 'PICS',
        'layout': 'max',
        'wm_class': [
            # 'sxiv',
            'feh',
            'nomacs',
        ],
        'wm_name':[],
    },
    {
        'key': '6',
        'label': '露  ₆',
        # 'label': '醙  ₆',
        'name': 'SONG',
        'layout': 'monadtall',
        'wm_class': [
            'yarock',
            'deadbeef',
            'spotify',
            'MellowPlayer',
            'de.haeckerfelix.Shortwave',
        ],
        'wm_name':[],
    },
    {
        'key': '7',
        # 'label': '磊  ₇',
        'label': '輸  ₇',
        'name': 'FILM',
        'layout': 'max',
        'wm_class': [
            # 'mpv',
            'vlc',
            'Gtk-pipe-viewer',
        ],
        'wm_name':[],
    },
    {
        'key': '8',
        'label': ' ',
        'name': 'FUN',
        'layout': 'max',
        'wm_class': [],
        'wm_name':['BpyTOP'],
    },
    {
        'key': '9',
        'label': '勇 ',
        'name': 'PRIV',
        'layout': 'monadtall',
        'wm_class': [
            'emacs',
            'vivaldi-stable',
        ],
        'wm_name':[
            '*vivaldi-*'
        ],
    },
    {
        'key': '0',
        'label': '變 ',
        'name': 'FIND',
        'layout': 'monadtall',
        'wm_class': [
            'qBittorrent',
        ],

        'wm_name':[],
    },
]


# ----------------------------
# ------ Floating Apps -------
# ----------------------------


flClass = [
    'toolbar',
    'confirmreset',
    'makebranch',
    'maketag',
    'Arandr',
    'Conky',
    'conky',
    'ssh-askpass',
    'Lxappearance',
    'Nm-connection-editor',
    # 'SpeedCrunch',
    'BleachBit'
]

flName = [
    'nmtui',
]
