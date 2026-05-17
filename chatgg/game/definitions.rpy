# -*- coding: utf-8 -*-
# ============================================================
# definitions.rpy — 全局变量与存档状态
# ============================================================

# --- 章节进度 ---
default chapter = 1
default chapter1_completed = False
default chapter2_completed = False
default chapter3_completed = False

# --- 核心数值 ---
default trust = 0
default insight = 0
default responsibility = 0
default integrity = 5
default empathy = 5
default resilience = 5

# --- 第一章相关变量 ---
default ch1_student_suicide_attempted = False
default ch1_linzixuan_outcome = ""
default ch1_choice_record = []
default ch1_met_zhouyaoqin = False
default ch1_reported_fake = False
default ch1_helped_student = False

# --- 第二章相关变量 ---
default ch2_discovered_anomaly = False
default ch2_reported = False
default ch2_accepted_temptation = False
default ch2_edge_person = False
default ch2_choice_record = []

# --- 第三章相关变量 ---
default ch3_trust_to_zhou = 0
default ch3_evidence_gathered = False
default ch3_betrayed = False
default ch3_retaliation = ""
default ch3_choice_record = []

# --- 悬疑线索系统 ---
default discovered_clues = []
default clue_linzixuan_secret = False
default clue_wangmei_hidden = False
default clue_academic_incident = False

# --- 结局相关标记 ---
default helped_student = False
default ignored_warning = False
default crossed_boundary = False
default told_truth = False
default chose_institution = False

# --- 对话分支记录 ---
default dialogue_history = []

# --- 学生池 ---
default student_pool = []
default current_student = None
default current_problem_type = None
default current_event_completed = False
