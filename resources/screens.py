#!/usr/bin/env python

# ====================================================
# SCREENS
# ~/.config/qtile/utils/screens.py
# ====================================================

# ----------------------------
# --------- Reference --------
# ----------------------------
# from libqtile.config import Screen
# from libqtile import bar, widget

# screens = [
#     Screen(
#         top=bar.Bar([
#             widget.GroupBox(),
#             widget.WindowName()
#         ], 30),
#     ),
#     Screen(
#         top=bar.Bar([
#             widget.GroupBox(),
#             widget.WindowName()
#         ], 30),
#     )
# ]

# ----------------------------
# ---------- Imports ---------
# ----------------------------

# === Standard === #

# === Third-Party === #
from libqtile import bar
from libqtile.config import Screen

# === Local === #
# from .groups import *
from .widgets import *


# ----------------------------
# --------- Widgets ----------
# ----------------------------


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=22,
                opacity=.90
            )
        ),
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen2(),
                size=26,
                opacity=0.90
            )
        )
    ]


screens = init_screens()
reconfigure_screens = True