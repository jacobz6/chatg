# -*- coding: utf-8 -*-
# ============================================================
# characters.rpy — 角色定义
# ============================================================

init python:
    shen_si = Character(
        "沈思",
        color="#5B7DB1",
        what_color="#E8E8E8"
    )

    narrator = Character(None, what_color="#AAAAAA")

    observe_text = Character(
        None,
        what_color="#7A9EC9",
        what_italic=True
    )

init python:
    lin_zixuan = Character(
        "林子轩",
        color="#D94A4A",
        what_color="#F0F0F0"
    )

    wang_yuqin = Character(
        "王雨晴",
        color="#4AD94A",
        what_color="#F0F0F0"
    )

    wang_director = Character(
        "王主任",
        color="#9A4AD4",
        what_color="#F0F0F0"
    )

    zhang_professor = Character(
        "张教授",
        color="#9A4AD4",
        what_color="#F0F0F0"
    )

    chen_professor = Character(
        "陈明德",
        color="#8B4513",
        what_color="#F0F0F0"
    )

    liu_jie = Character(
        "刘姐",
        color="#CCCCCC",
        what_color="#E0E0E0"
    )

    random_student = Character(
        "[temp_student_name]",
        color="#CCCCCC",
        what_color="#E0E0E0"
    )
