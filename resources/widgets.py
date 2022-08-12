# ====================================================
#
#!/usr/bin/env python
# coding=utf-8
# WIDGETS
# ~/.config/qtile/utils/widgets.py
#
# ====================================================

# ----------------------------
# ---------- Imports ---------
# ----------------------------

# === Standard === #
import subprocess

# === Third-Party === #
from libqtile import widget, qtile
from libqtile.widget.base import Mirror

# === Local === #
from .variables import *
from .groups import *
from .layouts import *
from .keys import *
from .battery import *

# ----------------------------
# --------- Defaults ---------
# ----------------------------


widget_defaults = dict(
    font=fontDisplay[0],
    fontsize=10,
    padding=2,
    foreground=colLight[0],
    background=colDark[0],
)

extension_defaults = widget_defaults.copy()


# ----------------------------
# ---------- Bar 1 -----------
# ----------------------------


def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(
            custom_icon_paths=qIcons,
            background=colDark[0],
            scale=0.5
        ),
        widget.AGroupBox(
            background=colDark[0],
            foreground=colAccent[0],
            fontsize=8,
            padding=10,
            borderwidth=0,
            mouse_callbacks={
                # Left
                'Button1': lambda: qtile.cmd_spawn(Launcher[0]),
                # Middle
                'Button2': lambda: qtile.cmd_spawn(Launcher[2]),
                # Right
                'Button3': lambda: qtile.cmd_spawn(Launcher[1]),
            }
        ),
        # widget.TextBox(
        #     font=fontIcon[0],
        #     text='•',
        #     fontsize=18,
        #     background=colDark[0],
        # ),
        widget.WindowName(
            foreground=colLight[0],
            background=colDark[0],
            padding=8,
        ),
        widget.WidgetBox(
            text_closed='',
            text_open='',
            font=fontIcon[1],
            fontsize=18,
            padding=0,
            close_button_location='right',
            foreground=colAccent[0],
            background=colDark[0],
            widgets=[
                widget.TextBox(
                    text=' ₿',
                    padding=0,
                    fontsize=12
                ),
                widget.BitcoinTicker(
                    padding=5,
                    mouse_callbacks={
                        'Button1': lambda:
                        qtile.cmd_spawn(
                            Calculator[0]
                        )
                    }
                ),
                widget.TextBox(
                    text=' 🖬',
                    padding=0,
                    fontsize=14
                ),
                widget.Memory(
                    padding=5,
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(
                            sysViewer
                        ),
                        'Button1':
                        lambda: qtile.cmd_spawn(
                            sysViewer
                        ),
                    }
                ),
                # widget.TextBox(
                #     text=' ⟳',
                #     padding=2,
                #     fontsize=14
                # ),
            ]
        ),
        widget.GenPollText(
            func=dateNow,
            update_interval=1,
            font=fontFancy[0],
            padding=10,
            foreground=colDark[1],
            background=colAccent[0],
        ),
        widget.CheckUpdates(
            update_interval=1800,
            distro='Arch_checkupdates',
            display_format='{updates} ',
            font=fontFancy[0],
            background=colAccent[0],
            # execute=appManager[1],
            mouse_callbacks={
                # Left
                'Button1': lambda: qtile.cmd_spawn(appManager[0]),
                # Middle
                'Button2': lambda: qtile.cmd_spawn(sysManager[0]),
                # Right
                'Button3': lambda: qtile.cmd_spawn(appManager[0]),
            }

        ),
        widget.WidgetBox(
            text_open='',
            text_closed='',
            font=fontIcon[1],
            fontsize=18,
            padding=0,
            close_button_location='left',
            foreground=colAccent[0],
            background=colDark[0],
            widgets=[
                widget.Net(
                    interface='wlo1',
                    font=fontDisplay[0],
                    format='{down}↓↑{up}',
                    padding=5,
                    mouse_callbacks={
                        # Left
                        'Button1': lambda: qtile.cmd_spawn(sysViewer[1]),
                        # Middle
                        'Button2': lambda: qtile.cmd_spawn(sysManager[0]),
                        # Right
                        'Button3': lambda: qtile.cmd_spawn(sysViewer[0]),
                    }
                ),
                widget.Volume(
                    # **widget_defaults,
                    emoji=True,
                    mouse_callbacks={
                        # Left
                        # 'Button1': lambda: qtile.cmd_spawn(sysManager[0]),
                        # Middle
                        'Button2': lambda: qtile.cmd_spawn(sysViewer[0]),
                        # Right
                        'Button3': lambda: qtile.cmd_spawn('htop'),
                    }
                ),
                BatteryIcon(
                    padding=0,
                    scale=0.7,
                    y_poss=2,
                    theme_path=qIcons,
                    update_interval=5,
                ),
            ]
        ),
        widget.Spacer(
            background=colDark[0]
        ),
        widget.Cmus(
            foreground=colLight[0],
            padding=10,
        ),
        widget.Moc(
            noplay_color=colLight[0],
        ),
        widget.GroupBox(
            background=colDark[0],
            active=colLight[0],
            inactive=colDark[2],
            block_highlight_text_color=colAccent[1],
            borderwidth=0,
            font=fontIcon[0],
            fontsize=14,
            urgent_alert_method='border',
            urgent_text=colAlert[0],
            urgent_border=colAlert[0],
            hide_unused=True,
            disable_drag=True,
        ),
        widget.GenPollText(
            update_interval=1,
            fontsize=16,
            func=lambda: subprocess.check_output(nm).decode(),
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(nmShow, shell=True),
                'Button3': lambda: qtile.cmd_spawn(nmUI, shell=True)
            }
        ),
        widget.Systray(
            # background=colAccent[0],
            # padding=2,
        ),
    ]
    return widgets_list
