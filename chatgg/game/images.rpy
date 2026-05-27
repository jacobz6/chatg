# -*- coding: utf-8 -*-
# ============================================================
# images.rpy - 图片资源定义文件
# ============================================================
# 此文件用于定义所有游戏使用的图片资源
# 图片会自动从对应文件夹加载，无需手动声明
#
# 文件夹结构：
#   images/bg/      - 场景背景
#   images/chars/   - 角色立绘
#   images/props/   - 道具/UI
# ============================================================

init python:
    # Ren'Py会自动从images文件夹加载图片
    # 图片会自动获得以下名称格式：
    #   bg_场景名  (来自images/bg/)
    #   角色名_表情 (来自images/chars/)
    #   props_道具名 (来自images/props/)
    #
    # 例如：
    #   images/bg/office_morning.png -> bg_office_morning
    #   images/chars/shen_si_normal.png -> shen_si_normal
    #   images/props/paper_diagnosis.png -> props_paper_diagnosis
    pass

# ============================================================
# 背景图片定义（占位说明）
# ============================================================
# 请将以下图片放入 images/bg/ 文件夹：
#   bg_office.png
#   bg_office_morning.png
#   bg_office_afternoon.png
#   bg_office_sunny.png
#   bg_office_director.png
#   bg_office_jiwei.png
#   bg_canteen.png
#   bg_dormitory.png
#   bg_apartment_night.png

# ============================================================
# 角色立绘定义（占位说明）
# ============================================================
# 请将以下图片放入 images/chars/ 文件夹：
#
# 沈思：
#   shen_si_normal.png
#   shen_si_concerned.png
#   shen_si_serious.png
#   shen_si_alarmed.png
#   shen_si_worried.png
#   shen_si_tired.png
#   shen_si_smiling.png
#   shen_si_sigh.png
#
# 林子轩：
#   lin_zixuan_normal.png
#   lin_zixuan_nervous.png
#   lin_zixuan_pale.png
#   lin_zixuan_hesitant.png
#   lin_zixuan_exhausted.png
#   lin_zixuan_confused.png
#   lin_zixuan_relieved.png
#   lin_zixuan_sad.png
#   lin_zixuan_terrified.png
#
# 王雨晴：
#   wang_yuqin_normal.png
#   wang_yuqin_sit.png
#   wang_yuqin_sad.png
#   wang_yuqin_crying.png
#
# 王主任：
#   wang_director_normal.png
#   wang_director_serious.png
#   wang_director_thinking.png
#   wang_director_alarmed.png
#
# 其他角色：
#   zhang_professor_normal.png
#   liu_jie_normal.png
#   chen_mingde_normal.png
#   zhang_jie_normal.png
#   sun_leader_normal.png
#   li_laoshi_normal.png
#   renshi_xiaoli_normal.png
#   xiao_zhou_normal.png
#   zhao_zuzhang_normal.png
#   linju_ayi_normal.png
#   wang_chuzhang_normal.png
#   sheng_jiwei_normal.png

# ============================================================
# 道具/UI图片定义（占位说明）
# ============================================================
# 请将以下图片放入 images/props/ 文件夹：
#   props_paper_diagnosis.png
#   props_paper_crumpled.png
