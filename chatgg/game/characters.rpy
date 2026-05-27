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

    # 第二章角色
    zhang_jie = Character(
        "张姐",
        color="#C8A87C",
        what_color="#F0F0F0"
    )

    sun_leader = Character(
        "孙领导",
        color="#8B0000",
        what_color="#F0F0F0"
    )

    li_laoshi = Character(
        "李老师",
        color="#6B8E23",
        what_color="#F0F0F0"
    )

    zhou_ming = Character(
        "周明",
        color="#4682B4",
        what_color="#F0F0F0"
    )

    renshi_xiaoli = Character(
        "人事处小李",
        color="#A0A0A0",
        what_color="#E0E0E0"
    )

    xiao_zhou = Character(
        "小周",
        color="#6CA6CD",
        what_color="#F0F0F0"
    )

    zhao_zuzhang = Character(
        "赵组长",
        color="#556B2F",
        what_color="#F0F0F0"
    )

    linju_ayi = Character(
        "邻居阿姨",
        color="#B8860B",
        what_color="#E0E0E0"
    )

    wang_chuzhang = Character(
        "王处长",
        color="#2F4F4F",
        what_color="#F0F0F0"
    )

    sheng_jiwei = Character(
        "省纪委工作人员",
        color="#4A4A4A",
        what_color="#E0E0E0"
    )

# ============================================================
# 角色立绘显示辅助函数
# ============================================================
# 使用方法：
#   $ show_char("shen_si", "normal", position="left")
#   $ hide_char("shen_si")
# ============================================================

# 角色立绘缩放配置
# 缩放因子：0.4表示将1440像素高度缩放到约576像素（更小，确保显示）
# 这样可以在1080像素的屏幕内完整显示，同时考虑文本框的空间
define char_zoom = 0.4

# 角色立绘显示的变换定义 - 使用更明确的语法
transform char_left(z=0.4):
    xpos 0.15
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    zoom z

transform char_center(z=0.4):
    xpos 0.5
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    zoom z

transform char_right(z=0.4):
    xpos 0.85
    ypos 1.0
    xanchor 0.5
    yanchor 1.0
    zoom z

# 居中显示变换（用于道具等）
transform center_full:
    xpos 0.5
    ypos 0.5
    xanchor 0.5
    yanchor 0.5

init python:
    def show_char(char_name, expression="normal", position="left", transition="dissolve", zoom=None):
        """
        显示角色立绘
        
        参数:
            char_name: 角色名称 (如 "shen_si", "lin_zixuan")
            expression: 表情 (如 "normal", "nervous")
            position: 位置 ("left", "center", "right")
            transition: 过渡效果 ("dissolve", "fade" 等)
            zoom: 自定义缩放比例（可选，如0.5）
        """
        img_name = f"{char_name}_{expression}"
        
        # 确定缩放比例
        use_zoom = zoom if zoom is not None else char_zoom
        
        # 直接使用Ren'Py的show语法，最可靠的方式
        if position == "left":
            if transition == "dissolve":
                renpy.show(img_name, at_list=[char_left(z=use_zoom)], with_none=False)
            else:
                renpy.show(img_name, at_list=[char_left(z=use_zoom)], with_none=True)
        elif position == "center":
            if transition == "dissolve":
                renpy.show(img_name, at_list=[char_center(z=use_zoom)], with_none=False)
            else:
                renpy.show(img_name, at_list=[char_center(z=use_zoom)], with_none=True)
        elif position == "right":
            if transition == "dissolve":
                renpy.show(img_name, at_list=[char_right(z=use_zoom)], with_none=False)
            else:
                renpy.show(img_name, at_list=[char_right(z=use_zoom)], with_none=True)
        else:
            if transition == "dissolve":
                renpy.show(img_name, at_list=[char_left(z=use_zoom)], with_none=False)
            else:
                renpy.show(img_name, at_list=[char_left(z=use_zoom)], with_none=True)
    
    def hide_char(char_name, transition="dissolve"):
        """
        隐藏角色立绘
        
        参数:
            char_name: 角色名称
            transition: 过渡效果
        """
        img_name = f"{char_name}_"
        if transition == "dissolve":
            renpy.hide(img_name)
        else:
            renpy.hide(img_name, with_none=True)
    
    def show_bg(bg_name, transition="fade"):
        """
        显示背景图片
        
        参数:
            bg_name: 背景名称 (如 "office_morning", "canteen")
            transition: 过渡效果
        """
        img_name = f"bg_{bg_name}"
        if transition == "fade":
            renpy.scene(img_name)
        else:
            renpy.scene(img_name, with_none=True)
    
    def show_prop(prop_name, position="center", transition="dissolve"):
        """
        显示道具/UI图片
        
        参数:
            prop_name: 道具名称 (如 "paper_diagnosis")
            position: 位置 ("left", "center", "right")
            transition: 过渡效果
        """
        img_name = f"props_{prop_name}"
        
        # 获取位置变换
        if position == "left":
            pos_transform = left
        elif position == "center":
            pos_transform = center_full
        elif position == "right":
            pos_transform = right
        else:
            pos_transform = center_full  # 默认居中
        
        if transition == "dissolve":
            renpy.show(img_name, at_list=[pos_transform])
        else:
            renpy.show(img_name, at_list=[pos_transform], with_none=True)

