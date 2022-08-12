# ====================================================
#
#!/usr/bin/env python
# coding=utf-8
# GROUPS
# ~/.config/qtile/utils/groups.py
#
# ====================================================


# ----------------------------
# ---------- Imports ---------
# ----------------------------

# === Standard === #

# === Third-Party === #
from libqtile.config import Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy

# === Local === #
from .variables import *
from .keys import *

# ----------------------------
# --------- GROUPS -----------
# ----------------------------

groups = []

for workspace in workspaces:
    gKey = workspace['key']
    gName = workspace['name']
    gLabel = workspace['label']
    gLayout = workspace['layout'].lower()
    gClass = Match(wm_class=workspace['wm_class'])
    gTitle = Match(title=workspace['wm_name'])

    # === Groups === #
    groups.append(
        Group(
            name=gName,
            label=gLabel,
            layout=gLayout,
            matches=gClass or gTitle,
        ),

    )

    groups.append(
        ScratchPad(
            "dropTerm", [
                DropDown(
                    "gTerm", Terminal[0],
                    opacity=0.98,
                    on_focus_lost_hide=True
                )
            ]
        ),
    )

# === KEYS === #
    keys.extend([
        Key(
            supW, gKey,
            lazy.group[gName].toscreen(),
            desc='Navigate workspaces {Grave,1,2,3,4,5,6,7,8,9,0}'
        ),
        Key(
            supS, gKey,
            lazy.window.togroup(gName),
            lazy.group[gName].toscreen(),
            desc='Move active window to selected workspace and navigate there'
        ),
        Key(
            supC, gKey,
            lazy.window.togroup(gName),
            desc='Move active window to selected workspace'
        ),
        Key(
            ctl, 'F12',
            lazy.group['scratchpad'].dropdown_toggle("gTerm"),
            desc='Dropdown default Terminal'
        ),
    ])

# ----------------------------
# -------- FUNCTIONS ---------
# ----------------------------


@ lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@ lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'focus'
