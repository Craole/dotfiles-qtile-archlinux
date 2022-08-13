#!/usr/bin/env python

# ====================================================
# KEYS
# ~/.config/qtile/utils/keys.py
# ====================================================


# ----------------------------
# ---------- Imports ---------
# ----------------------------

# === Standard === #
from typing import List  # noqa: F401

# === Third-Party === #
from libqtile.command import lazy
from libqtile.config import Click, Drag, KeyChord, Key

# === Local === #
from .variables import *


# ----------------------------
# --------- Hotkeys ----------
# ----------------------------

keys = [

    #=== Key File ===#
    Key(
        supW, 'comma',
        lazy.spawn(q_keymap),
        desc='Open Keys.py'
    ),

    #=== Qtile Control ===#
    Key(
        supC, 'q',
        lazy.shutdown()
    ),
    Key(
        supC, 'F4',
        lazy.shutdown()
    ),
    Key(
        supC, 'r',
        lazy.restart()
    ),
    Key(
        supA, 'F5',
        lazy.restart()
    ),

    #=== Groups/Workspaces ===#
    Key(
        supA, 'Tab',
        lazy.screen.toggle_group(),
        desc='Move to previously visited group'
    ),
    Key(
        supW, 'Tab',
        lazy.screen.next_group(),
        desc='Move to next group (clockwise)'
    ),
    Key(
        supS, 'Tab',
        lazy.screen.prev_group(),
        desc='Move to previous group (anti-clockwise)'
    ),

    #=== Window/Layout ===#
    Key(
        supW, 'q',
        lazy.window.kill(),
        desc='Close active window'
    ),
    Key(
        alt, 'q',
        lazy.window.kill(),
        desc='Close active window'
    ),
    Key(
        supS, 'q',
        lazy.spawn(appKill[0]),
        desc='Force close sleceted window'
    ),
    Key(
        alt, 'F4',
        lazy.window.kill(),
        desc='Close active window'
    ),
    Key(
        altS, 'Return',
        lazy.window.toggle_fullscreen(),
        desc='Put the focused window to/from fullscreen mode'
    ),
    Key(
        altC, 'Return',
        lazy.window.toggle_floating(),
        desc='Put the focused window to/from floating mode'
    ),
    Key(
        alt, 'Prior',
        lazy.prev_layout(),
        desc='Use next layout'
    ),
    Key(
        alt, 'Next',
        lazy.next_layout(),
        desc='Use next layout'
    ),
    Key(
        alt, 'End',
        lazy.layout.maximize()
    ),
    Key(
        altS, 'End',
        lazy.layout.normalize()
    ),
    Key(
        alt, 'Home',
        lazy.layout.reset()
    ),
    Key(
        alt, 'KP_Divide',
        lazy.layout.shrink(),
        desc='Decrease space occupied by secondary window'
    ),
    Key(
        alt, 'KP_Multiply',
        lazy.layout.grow(),
        desc='Increase space occupied by secondary window'
    ),
    Key(
        alt, 'KP_Subtract',
        lazy.layout.shrink_main(),
        lazy.layout.decrease_ratio(),
        # lazy.layout.decrease_nmaster(),
        desc='Decrease space occupied by master window'
    ),
    Key(
        alt, 'KP_Add',
        lazy.layout.grow_main(),
        lazy.layout.increase_ratio(),
        # lazy.layout.increase_nmaster(),
        desc='Increase space occupied by master window'
    ),
    Key(
        alt, 'Tab',
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
    ),
    Key(
        altS, 'Tab',
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),
    Key(
        altS, 'KP_Subtract',
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
    ),
    Key(
        altS, 'KP_Add',
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
    ),
    Key(
        alt, 'space',
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies'
    ),
    Key(
        supA, 'space',
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'),
    Key(
        supC, 'KP_Subtract',
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
    ),
    Key(
        altC, 'KP_Add',
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
    ),

    #=== Function Keys ===#
    Key(
        supW, 'F1',
        lazy.spawn(videoPlayer[0])
    ),
    Key(
        [], 'XF86MonBrightnessDown',
        lazy.spawn(bclDown[0])
    ),
    Key(
        [], 'XF86MonBrightnessUp',
        lazy.spawn(bclUp[0])
    ),
    Key(
        [], 'XF86AudioMute',
        lazy.spawn(volMute[0])
    ),
    Key(
        [], 'XF86AudioLowerVolume',
        lazy.spawn(volDown[0])
    ),
    Key(
        [], 'XF86AudioRaiseVolume',
        lazy.spawn(volUp[0])
    ),
    Key(
        [], 'XF86AudioPrev',
        lazy.spawn()
    ),
    Key(
        [], 'XF86AudioPlay',
        lazy.spawn(mediaPlayer[0])
    ),
    Key(
        [], 'XF86AudioNext',
        lazy.spawn()
    ),
    # Key(
    #     [], 'XF86RFKill',
    #     lazy.spawn()
    # ),

    #=== Apps ===#

    # Key(
    #     ctlS, 'p', ===
    #     subprocess.call([picom]),
    #     desc='Toggle compositor effects'
    # ),
    Key(
        supW, 'F1',
        lazy.spawn(screenLock[0]),
        desc='Lockscreen'
    ),
    Key(
        ctl, 'Escape',
        lazy.spawn(sysViewer[0])
    ),
    Key(
        ctlS, 'Escape',
        lazy.spawn(sysManager[0])
    ),
    Key(
        alt, 'F2',
        lazy.spawn(dMenu[0])
    ),
    Key(
        supW, 'space',
        lazy.spawn(dMenu[0])
    ),
    Key(
        ctl, 'space',
        lazy.spawn(Launcher[1])
    ),
    # Key(
    #     supW, 'r',
    #     lazy.spawn(Launcher[1])
    # ),
    Key(
        supW, 'Return',
        lazy.spawn(Terminal[2])
    ),
    Key(
        ctl, 'grave',
        lazy.spawn(Terminal[0])
    ),
    Key(
        alt, 't',
        lazy.spawn(Terminal[0])
    ),
    Key(
        ctlS, 'grave',
        lazy.spawn(Terminal[1])
    ),
    Key(
        supW, 'e',
        lazy.spawn(guiFM[0]),
        desc='Default IDE or Visual Editor'
    ),
    Key(
        supS, 'e',
        lazy.spawn(guiFM[1])
    ),
    Key(
        ctlS, 'e',
        lazy.spawn(guiFM[2])
    ),
    Key(
        alt, 'e',
        lazy.spawn(termFM[0])
    ),
    Key(
        altS, 'e',
        lazy.spawn(termFM[1])
    ),
    Key(
        supW, 'c',
        lazy.spawn(iDE[0]),
        desc='Default IDE or Visual Editor'
    ),
    Key(
        supA, 'e',
        lazy.spawn(Editor[0]),
        desc='Default Editor'
    ),
    Key(
        supW, 'd',
        lazy.spawn(VSCode[1])
    ),
    Key(
        supS, 'd',
        lazy.spawn(VSCode[2])
    ),
    Key(
        supW, 'b',
        lazy.spawn(Browser[0])
    ),
    Key(
        supS, 'b',
        lazy.spawn(Browser[1])
    ),
    Key(
        supW, 'r',
        lazy.spawn(radioPlayer[0])
    ),
    Key(
        supS, 'p',
        lazy.spawn(radioPlayer[0])
    ),
    Key(
        supW, 'f',
        lazy.spawn(fontManager[0])
    ),
    Key(
        supW, 'KP_Add',
        lazy.spawn(Calculator[0])
    ),
    Key(
        supW, 't',
        lazy.spawn(Downloader[0])
    ),
    Key(
        alt, 'm',
        lazy.spawn(eMail[0])
    ),
    Key(
        alt, 'c',
        lazy.spawn(colorPicker[0])
    ),
    Key(
        supA, 'x',
        lazy.spawn(appKill[0])
    ),
    Key(
        ctlS, 'Escape',
        lazy.spawn(
            sysManager
        )
    ),
    Key(
        alt, 'x',
        lazy.spawn(
            xev
        )
    ),
    Key(
        supW, 'a',
        lazy.spawn(
            appManager
        )
    ),
    Key(
        supW, 'y',
        lazy.spawn(
            YouTube
        )
    ),

    # #=== Emacs programs launched using the key chord CTRL+e followed by 'key'
    KeyChord(
        ctl, 'e', [
            Key(
                [], 'e',
                lazy.spawn(Emacs[0])
            ),
            Key(
                [], 'b',
                lazy.spawn(Emacs[1])
            ),
            Key(
                [], 'd',
                lazy.spawn(Emacs[2])
            ),
            Key(
                [], 'i',
                lazy.spawn(Emacs[3])
            ),
            Key(
                [], 'm',
                lazy.spawn(Emacs[4])
            ),
            Key(
                [], 'n',
                lazy.spawn(Emacs[5])
            ),
            Key(
                [], 's',
                lazy.spawn(Emacs[6])
            ),
            Key(
                [], 'v',
                lazy.spawn(Emacs[7])
            ),
        ]
    ),
    # === Dmenu scripts launched using the key chord SUPER+p followed by 'key'
    KeyChord(
        # supW, 'space', [
        supW, 'p', [
            Key(
                [], 'e',
                lazy.spawn(dMenu[1])
            ),
            Key(
                [], 'i',
                lazy.spawn(dMenu[2])
            ),
            Key(
                [], 'k',
                lazy.spawn(dMenu[3])
            ),
            Key(
                [], 'l',
                lazy.spawn(dMenu[4])
            ),
            Key(
                [], 'm',
                lazy.spawn(dMenu[5])
            ),
            Key(
                [], 'r',
                lazy.spawn(dMenu[6])
            ),
            Key(
                [], 's',
                lazy.spawn(dMenu[7])
            ),
            Key(
                [], 'p',
                lazy.spawn(dMenu[8])
            ),
        ]
    ),
]

mouse = [
    Drag(
        supW, 'Button1',
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
        desc='Hold the mod key to drag windows with the left mouse button'
    ),
    Click(
        supW, 'Button2',
        lazy.window.bring_to_front(),
        desc='Float window with the middle mouse button'
    ),
    Drag(
        supW, 'Button3',
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
        desc='Hold the mod key to resize the windows with the right button'
    )
]
