# -*- coding: utf-8 -*-
# ============================================================
# script.rpy — 入口文件
# ============================================================

init python:
    import os
    import random

init -1:
    image bg black = "#000000"
    image bg office = "#2C3E50"
    image bg corridor = "#34495E"
    image linzixuan = Text("林子轩", size=40, color="#D94A4A")
    image wangmei = Text("王梅", size=40, color="#4AD94A")

screen main_menu():
    tag menu
    add gui.main_menu_background

    frame:
        xalign 0.5
        yalign 0.5
        padding (60, 40)
        background Frame("gui/game_menu.png", 10, 10)

        vbox:
            spacing 20
            text "高校辅导员" size 50 color "#FFFFFF" xalign 0.5
            text "——你的每一个选择，都将影响某个人的命运——" size 20 color "#AAAAAA" xalign 0.5

            null height 20

            textbutton "开始游戏" action Start() xalign 0.5
            textbutton "继续游戏" action Return() xalign 0.5
            textbutton "设置" action ShowMenu("preferences") xalign 0.5
            textbutton "退出" action Quit(confirm=not renpy.variant("mobile")) xalign 0.5

label before_main_menu:
    return

label main_menu:
    call screen main_menu
    return

label start:
    $ chapter = 1
    $ trust = 0
    $ insight = 0
    $ responsibility = 0
    $ discovered_clues = []
    $ helped_student = False
    $ ignored_warning = False
    $ crossed_boundary = False
    $ told_truth = False
    $ chose_institution = False
    $ dialogue_history = []
    $ student_pool = []
    $ current_student = None

    call chapter1_start

    if chapter1_completed:
        jump chapter2_start

    return

label chapter2_start:
    scene black with fade
    narrator "【第二章 · 暗流涌动 — 施工中】"
    narrator "感谢游玩第一章！"
    return

label chapter3_start:
    scene black with fade
    narrator "【第三章 · 终章 — 施工中】"
    return
