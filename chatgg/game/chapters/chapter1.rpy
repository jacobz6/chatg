# -*- coding: utf-8 -*-
# ============================================================
# chapter1.rpy — 第一章：论文风云
# ============================================================

label chapter1_start:
    jump chapter1

label chapter1:
    # 全局变量安全初始化（防止未定义导致崩溃）
    python:
        for var_name in ['responsibility', 'empathy', 'insight', 'resilience', 'integrity']:
            if var_name not in globals():
                globals()[var_name] = 5
    
    # 本章增量追踪变量（用于正确显示数值变化）
    $ ch1_integrity_delta = 0
    $ ch1_insight_delta = 0
    $ ch1_empathy_delta = 0
    $ ch1_resilience_delta = 0
    
    # 重置本章变量
    $ ch1_student_suicide_attempted = False
    $ ch1_linzixuan_outcome = ""
    $ ch1_choice_record = []
    $ ch1_reported_fake = False
    $ ch1_helped_student = False

    scene black with fade
    pause 0.5

    # 章节标题
    show text "第一章：论文风云" with dissolve
    pause 2
    hide text with dissolve

    # ============================================================
    # 场景1：办公室 · 清晨
    # ============================================================
    scene bg_office_morning with fade

    narrator "五月的广州，回南天刚过，潮湿的空气里弥漫着初夏的黏腻。"
    narrator "研究生院办公室的百叶窗半开着，晨光穿过叶片间隙，在办公桌上投下细密的光条纹。"
    narrator "墙上挂着'明德博学，求是创新'的院训，旁边是一排整齐的文件柜。"

    narrator "沈思比平时早到了二十分钟。作为研究生院教务干事，她早已习惯了在正式上班前先理一理今天的工作。"
    narrator "这几天是毕业论文提交的冲刺期，电话和邮件都会比平时多出三四倍。"

    shen_si "（端起茶杯抿了一口）今天的待办事项可真不少..."

    narrator "她给自己泡了杯从化橘红茶，据说能缓解咽炎。打开电脑，桌面上的待办事项清单密密麻麻。"
    narrator "今天最重要的一项是核查所有超期提交的学生的特殊情况申请。"

    narrator "「咚咚咚——」"
    narrator "有人在敲门，节奏有点犹豫，不像平时那些雷厉风行的学生干部。"

    show lin_zixuan_normal at left
    with dissolve

    lin_zixuan "沈老师，早上好……打扰您了。"

    shen_si "请坐吧，什么事？"

    lin_zixuan "（坐下，将档案袋放在膝盖上）沈老师，我……我有件事想跟您商量。"

    shen_si "别紧张，慢慢说。"

    lin_zixuan "是这样的，我的论文……导师老张不让我送审。"

    shen_si "不让你送审？子轩，你知道今年论文提交的截止日期是5月20号，今天已经17号了……"

    lin_zixuan "我知道，我知道的，沈老师。（语速加快）但我真的有特殊情况……"

    # 选择分支1
    menu ch1_choice_1:
        "按规定，超期申请需要院长审批，而且时间这么紧，恐怕很难……" :  # 规则优先
            $ ch1_choice_record.append("ch1_1_A")
            $ responsibility += 1
            shen_si "按规定，超期申请需要院长审批，而且时间这么紧，恐怕很难。你应该早点准备的。"
            jump ch1_scene1_branch_A
        
        "（身体微微前倾，认真地看着他）" :  # 耐心倾听
            $ ch1_choice_record.append("ch1_1_B")
            $ empathy += 1
            $ ch1_empathy_delta += 1
            shen_si "（身体微微前倾）什么特殊情况？能说说吗？"
            jump ch1_scene1_branch_B
        
        "这个时间点很敏感，所有流程都要按规矩来。你应该清楚后果。" :  # 严肃警告
            $ ch1_choice_record.append("ch1_1_C")
            $ responsibility += 1
            shen_si "这个时间点很敏感，所有流程都要按规矩来。你应该清楚后果。"
            jump ch1_scene1_branch_C

    # 分支A：规则优先
    label ch1_scene1_branch_A:
        lin_zixuan "（脸色发白）可是……我签了工作，要是拿不到学位……"
        lin_zixuan "沈老师，求您了，给我一次机会……"
        
        show lin_zixuan_nervous with dissolve
        shen_si "我理解你的心情，但制度就是制度。你先回去吧，我会按流程处理。"
        jump ch1_scene2

    # 分支B：耐心倾听（主要分支）
    label ch1_scene1_branch_B:
        lin_zixuan "（声音有些哽）沈老师，其实我……我签了一家深圳的公司，年薪三十五万。"
        lin_zixuan "他们要求6月1号之前拿到双证，否则offer就作废了。"
        
        shen_si "这是好事啊。"

        lin_zixuan "是好消息，但……（眼神黯淡）从四月中旬开始，张老师就说论文的统计分析逻辑有问题。"
        lin_zixuan "我改了两版，他说结论不够凝练……前前后后折腾了快一个月了。"

        shen_si "所以你现在的论文状态是……"

        lin_zixuan "（低下头）还在修改。我通宵改了一周了，真的……沈老师，我快撑不住了。"

        narrator "就在这时，林子轩像是下定了什么决心似的，打开了手里的档案袋，从里面抽出一张纸。"

        lin_zixuan "沈老师，这是我上个月的急诊病历和住院证明。我——我急性阑尾炎发作，在省人民医院做了手术。"

        show image "gui/paper_diagnosis.png" at right with dissolve
        pause 1

        shen_si "（仔细端详着诊断证明）手术……阑尾切除术？"

        lin_zixuan "（点头如捣蒜）对对对，就是这个。"

        shen_si "（沉默了几秒，手指轻轻敲击桌面）子轩，你说你在省人民医院做的手术？"

        lin_zixuan "（眼神闪烁了一下）对……对啊，有什么问题吗？"

        # 选择分支2
        menu ch1_choice_2:
            "省人民医院的诊断证明这里会有15位电子病历号，你的这张是空的。而且这纸张……" :  # 当场指出疑点
                $ ch1_choice_record.append("ch1_2_A")
                $ insight += 1
                $ ch1_insight_delta += 1
                jump ch1_scene1_branch_B_a
            
            "这样吧，材料我先收下，学院会按流程发公函核实。你先回去等通知。" :  # 程序处理
                $ ch1_choice_record.append("ch1_2_B")
                $ responsibility += 1
                jump ch1_scene1_branch_B_b
            
            "4月12日？那你出院后这一个月都在做什么？论文改得怎么样了？" :  # 转移话题
                $ ch1_choice_record.append("ch1_2_C")
                $ insight += 1
                $ ch1_insight_delta += 1
                jump ch1_scene1_branch_B_c

        # 分支B_a：当场指出疑点
        label ch1_scene1_branch_B_a:
            shen_si "子轩，你看这里——省人民医院的正规诊断证明，都会在这个位置打印15位的电子病历号。"
            shen_si "你的这张……是空的。"
            shen_si "还有这个章……边缘太模糊了，不像是铜章盖出来的。更像是……喷墨打印机打出来的。"
            
            show lin_zixuan_pale with dissolve
            lin_zixuan "（声音发颤）我……我不懂这些……医院给我的就是这样的……"
            
            shen_si "我不是在质疑你。只是按规定，这类材料我们必须核实。你先回去，我会联系医院确认。"
            
            lin_zixuan "（猛地站起来）沈老师！求求您……我真的没办法了……"
            
            shen_si "（抬手示意他坐下）坐下说。我在听。"
            
            lin_zixuan "（瘫坐在椅子上，声音哽咽）是假的……证明是假的……"
            
            shen_si "（沉默片刻）我知道。"
            
            lin_zixuan "（突然崩溃）我爹把牛卖了供我读书……我哥三十了还没结婚就为了供我……"
            lin_zixuan "张老师不让我过，我真的……真的没路了……"
            
            show shen_si_concerned with dissolve
            shen_si "（递给他一张纸巾）我理解你的压力。但造假解决不了问题。"
            
            lin_zixuan "（擦着眼泪）那我该怎么办……offer没了，学位也没了……我就是个废物……"
            
            shen_si "（语气坚定）学位还没没。你论文框架完成多少了？"
            
            lin_zixuan "（愣了一下）90%……就差数据分析那章……"
            
            shen_si "把论文发给我。我帮你看看能不能和张老师协调。"
            
            lin_zixuan "（抬起头，眼里有了光）真的？"
            
            shen_si "但造假这件事，我必须按程序上报。这是底线。"
            
            $ ch1_reported_fake = True
            $ ch1_helped_student = True
            jump ch1_scene2

        # 分支B_b：程序处理
        label ch1_scene1_branch_B_b:
            shen_si "这样吧，这份材料我先收下。按照学院规定，我们需要向省人民医院发公函核实。"
            shen_si "你先回去，保持手机畅通，有结果我会第一时间通知你。"
            
            lin_zixuan "（急切地）那需要多久？我……我时间真的很紧……"
            
            shen_si "公函流程大概需要3-5个工作日。如果核实无误，我们会尽快帮你走延毕申请。"
            shen_si "（意味深长地）当然，如果核实过程中发现问题……后果你应该清楚。"
            
            show lin_zixuan_pale with dissolve
            lin_zixuan "我……我知道了。谢谢沈老师。"
            
            jump ch1_scene2

        # 分支B_c：转移话题
        label ch1_scene1_branch_B_c:
            shen_si "4月12日做的手术，住院一周……那你出院后这一个月都在做什么？"
            shen_si "论文改得怎么样了？"
            
            lin_zixuan "（没想到她会这么问，愣了一下）我……我一直在改……张老师还是不满意……"
            
            shen_si "具体哪里不满意？数据分析？还是结论部分？"
            
            lin_zixuan "都有……他说我的统计方法有问题，结论站不住脚……"
            
            shen_si "（拿起笔在便签上记录）你现在每天能花多少时间在论文上？"
            
            lin_zixuan "（低下头）大部分时间……但有时候……（欲言又止）"
            
            shen_si "有时候什么？"
            
            lin_zixuan "有时候觉得……很累……不想动……"
            
            shen_si "我明白了。这样，你先把最新版的论文发给我。"
            shen_si "诊断证明我也收下，但我需要你签一份知情同意书——我们会发公函给医院核实。"
            
            show lin_zixuan_hesitant with dissolve
            lin_zixuan "（接过同意书）……好。"
            
            jump ch1_scene2

    # 分支C：严肃警告
    label ch1_scene1_branch_C:
        lin_zixuan "（低下头）我知道……但我真的没办法了……"
        lin_zixuan "沈老师，求您通融一下……"
        
        shen_si "通融？那对其他按时完成的同学公平吗？你先回去吧。"
        jump ch1_scene2

    # ============================================================
    # 场景2：核实 · 当天下午
    # ============================================================
    label ch1_scene2:
        scene bg_office_afternoon with fade
        hide image "gui/paper_diagnosis.png"
        
        narrator "午休时间，办公室的其他同事都去吃饭或者午睡了。"
        narrator "沈思一个人坐在工位上，面前摆着林子轩那份诊断证明和他刚发来的论文。"
        
        narrator "她已经给省人民医院打了电话，核实结果正如她所料——"
        narrator "4月12日确实有个叫'林子轩'的患者在省医就诊，但那是位68岁的老人，做的是白内障手术。"
        
        show shen_si_serious with dissolve
        shen_si "（在便签上记录）核实结果：诊断证明系伪造。"
        
        narrator "就在这时，办公室的门被推开了。进来的是王主任。"
        
        show wang_director with dissolve
        wang_director "小沈，听说有个叫林子轩的学生找你办超期？"
        
        shen_si "（站起身）王主任，是的。材料我已经核实过了——诊断证明是假的。"

        # 选择分支3
        menu ch1_choice_3:
            "诊断证明是伪造的，我建议直接驳回申请，按规定上报学生处处理。" :  # 严格执行
                $ ch1_choice_record.append("ch1_3_A")
                $ responsibility += 1
                $ ch1_integrity_delta += 2
                jump ch1_scene2_branch_A
            
            "诊断证明确实有问题，但我看了他的论文，完成度有90，只是数据分析需要指导。" :  # 争取机会
                $ ch1_choice_record.append("ch1_3_B")
                $ empathy += 1
                $ ch1_empathy_delta += 1
                jump ch1_scene2_branch_B
            
            "材料核实有问题，学生状态不对劲，我担心……" :  # 关注状态
                $ ch1_choice_record.append("ch1_3_C")
                $ empathy += 1
                $ ch1_empathy_delta += 1
                jump ch1_scene2_branch_C

        # 分支A：严格执行
        label ch1_scene2_branch_A:
            shen_si "诊断证明是伪造的，省医那边已经确认过了——4月12日登记的'林子轩'是位68岁的老人。"
            shen_si "我建议直接驳回申请，并按规定上报学生处处理。"
            
            show wang_director_serious with dissolve
            wang_director "（接过材料，眉头紧锁）又是造假……（叹气）按规矩来吧。这种风气不能助长。"
            
            shen_si "我这就起草处理意见。"
            
            wang_director "不过……注意方式方法。最近学生心理问题挺多的。"
            
            shen_si "（明白地点头）我会注意的。"
            
            $ ch1_reported_fake = True
            jump ch1_scene3

        # 分支B：争取机会
        label ch1_scene2_branch_B:
            shen_si "王主任，诊断证明确实有问题——省医核实过，4月12日的'林子轩'是位68岁的老人。"
            shen_si "但他的论文其实完成度很高，90%都做完了，就是数据分析那一章需要指导。"
            shen_si "如果直接驳回，他这个学就白上了……张导师那边我去协调，再给他两周时间，应该能改完。"
            
            wang_director "（犹豫地）这不合规矩啊……"
            
            shen_si "特殊情况特殊处理？而且造假这件事，我可以记在内部档案里，不公开通报，给他一次机会。"
            
            show wang_director_thinking with dissolve
            wang_director "（沉默良久）……你看着办吧。但出了问题，你要负责。"
            
            shen_si "（坚定地）我负责。"
            
            $ ch1_helped_student = True
            jump ch1_scene3

        # 分支C：关注状态
        label ch1_scene2_branch_C:
            shen_si "王主任，材料核实确实有问题——诊断证明是伪造的。"
            shen_si "但这个学生状态很不对劲。我跟他谈话的时候，他手一直在抖，眼神也不对……"
            shen_si "说什么'没路了'之类的话。"
            
            show wang_director_alarmed with dissolve
            wang_director "他说什么了？"
            
            shen_si "具体倒没说什么，但我担心他会不会有极端想法。今年就业压力这么大……"
            
            wang_director "你觉得……"
            
            shen_si "要不这样，先不忙着处理。我先联系他导师，看看能不能在论文上帮帮他。"
            shen_si "心理中心那边，也得打个招呼。"
            
            wang_director "（点头）安全第一。那就按你说的办。注意留痕。"
            
            shen_si "明白。"
            
            jump ch1_scene3

    # ============================================================
    # 场景3：食堂 · 傍晚
    # ============================================================
    label ch1_scene3:
        scene bg_canteen with fade
        
        narrator "傍晚六点半，研究生院食堂二楼。沈思端着餐盘找了个靠窗的位置坐下。"
        narrator "手机屏幕亮了，是刘姐发来的消息。"
        
        observe_text "【刘姐】沈思，听说今天有个学生找你办超期？小心点，上次有个学生被拒了，直接在网上发帖骂学院。"
        
        shen_si "（回复）知道了，谢谢提醒。"
        
        narrator "她放下手机，刚要吃饭，一个清亮的声音传来。"
        
        show wang_yuqin with dissolve
        wang_yuqin "沈老师！"

        # 选择分支4
        menu ch1_choice_4:
            "看到是王雨晴，立刻警惕地放下筷子：'你是为林子轩来的吧？'" :  # 主动出击
                $ ch1_choice_record.append("ch1_4_A")
                $ insight += 1
                $ ch1_insight_delta += 1
                jump ch1_scene3_branch_A
            
            "微笑着招手：'雨晴啊，来坐。'" :  # 保持友好
                $ ch1_choice_record.append("ch1_4_B")
                $ empathy += 1
                $ ch1_empathy_delta += 1
                jump ch1_scene3_branch_B
            
            "继续吃饭，头也不抬：'有事吗？'" :  # 保持距离
                $ ch1_choice_record.append("ch1_4_C")
                $ responsibility += 1
                jump ch1_scene3_branch_C

        # 分支A：主动出击
        label ch1_scene3_branch_A:
            shen_si "（放下筷子，看着她）你是为林子轩来的吧？"
            
            wang_yuqin "（愣住，随即低下头）是……沈老师，您都知道了？"
            
            shen_si "（点头）诊断证明是假的。"
            
            wang_yuqin "（声音发颤）我知道……但子轩他……他真的快撑不住了。"
            wang_yuqin "昨天在实验室，他突然说'活着有什么意思'，我们都吓坏了……"
            
            show shen_si_alarmed with dissolve
            shen_si "你们没告诉导师？"
            
            wang_yuqin "（苦笑）张导师忙着项目，根本不管这些……沈老师，求您了，给他一条路吧……"
            
            shen_si "（沉默片刻）你先坐下。跟我说说，他最近具体是什么状态。"
            
            jump ch1_scene4

        # 分支B：保持友好
        label ch1_scene3_branch_B:
            shen_si "（微笑着招手）雨晴啊，来坐。正好，我还想找你了解点情况呢。"
            
            show wang_yuqin_sit with dissolve
            wang_yuqin "（在对面坐下，有些紧张）沈老师，您……您想知道什么？"
            
            shen_si "先别说别的，你跟我说说，林子轩最近在实验室……状态怎么样？"
            
            show wang_yuqin_sad with dissolve
            wang_yuqin "很差……经常一个人发呆，上周组会PPT都念不下去……昨天还说'活着没意义'……"
            
            shen_si "（放下茶杯）他导师知道吗？"
            
            wang_yuqin "（摇头）张老师太忙了……沈老师，您能不能……"
            
            shen_si "（抬手示意她别说）我知道了。你放心，我会想办法。"
            
            jump ch1_scene4

        # 分支C：保持距离
        label ch1_scene3_branch_C:
            shen_si "（继续吃饭，头也不抬）有事吗？"
            
            wang_yuqin "（站在原地，有些尴尬）沈老师……我想跟您说说子轩的事……"
            
            shen_si "（放下勺子，擦了擦嘴）诊断证明是假的，这件事已经定性了。我没办法帮他。"
            
            wang_yuqin "（声音发颤）不是……沈老师，我不是来求您造假的。我是担心……担心子轩他……"
            
            shen_si "（终于抬头看她）他怎么了？"
            
            show wang_yuqin_crying with dissolve
            wang_yuqin "（眼泪掉下来）他昨天说'活着有什么意思'……我们都不敢离开他……"
            
            show shen_si_worried with dissolve
            shen_si "你们为什么不早说？"
            
            jump ch1_scene4

    # ============================================================
    # 场景4：宿舍楼 · 夜
    # ============================================================
    label ch1_scene4:
        scene bg_dormitory with fade
        
        narrator "东区学7栋404室，沈思站在门口。门开着一条缝，里面传来键盘敲击声。"
        
        shen_si "子轩，是我。"
        
        show lin_zixuan_exhausted with dissolve
        lin_zixuan "（惊讶）沈老师？您怎么……"
        
        shen_si "宿管那边我登记过了。"
        
        narrator "宿舍里乱糟糟的，只有林子轩一个人。他的电脑屏幕上，论文文档还开着。"
        
        shen_si "（走到桌前，看着屏幕）这是最新版？"
        
        lin_zixuan "（低下头）是……"

        # 选择分支5
        menu ch1_choice_5:
            "指着电脑屏幕：'数据分析这里用错了模型，应该用混合效应模型，不是普通线性回归。'" :  # 专业指导
                $ ch1_choice_record.append("ch1_5_A")
                $ insight += 1
                $ ch1_insight_delta += 2
                jump ch1_scene4_branch_A
            
            "在他对面坐下：'我知道你压力很大。但造假解决不了问题，只会让事情更糟。'" :  # 先共情
                $ ch1_choice_record.append("ch1_5_B")
                $ empathy += 1
                $ ch1_empathy_delta += 1
                jump ch1_scene4_branch_B
            
            "拿起桌上揉皱的诊断证明：'我已经知道这是假的。但我没上报——给你最后一次机会。'" :  # 摊牌施压
                $ ch1_choice_record.append("ch1_5_C")
                $ responsibility += 1
                jump ch1_scene4_branch_C

        # 分支A：专业指导
        label ch1_scene4_branch_A:
            shen_si "数据分析这里用错了模型，应该用混合效应模型，不是普通线性回归。"
            shen_si "这就是张老师说的'逻辑问题'。"
            
            show lin_zixuan_confused with dissolve
            lin_zixuan "我……我不知道……"
            
            shen_si "（拉过一把椅子坐下）来，我给你讲一遍。首先，你的自变量……"
            
            narrator "她开始耐心地讲解统计方法，手指在屏幕上滑动。"
            narrator "林子轩渐渐抬起头，眼里的迷茫慢慢变成专注。"
            
            lin_zixuan "（恍然大悟）原来是这样……我一直搞不懂为什么结果不对……"
            
            shen_si "（停下来，看着他）论文的问题能解决。但造假的事，你必须写份检讨。"
            
            show lin_zixuan_relieved with dissolve
            lin_zixuan "我写……我明天就交给您……"
            
            jump ch1_scene5

        # 分支B：先共情
        label ch1_scene4_branch_B:
            shen_si "（在他对面坐下，声音放轻）我知道你压力很大。"
            shen_si "签了工作，怕拿不到学位，怕对不起家里……"
            
            show lin_zixuan_sad with dissolve
            lin_zixuan "（眼圈红了）我爹把牛卖了……就为了给我凑学费……"
            
            shen_si "（点头）我理解。但你要知道，造假解决不了问题，只会让事情更糟。"
            
            lin_zixuan "（沉默良久）我……我只是太急了……"
            
            shen_si "（从包里拿出一份论文修改建议）急没用。来，我帮你看看论文。"
            shen_si "张老师说的问题，其实没那么难解决。"
            
            lin_zixuan "（抬起头，眼里有了希望）您……您愿意帮我？"
            
            shen_si "（递给他建议）这是我整理的修改思路。但造假这件事，必须按程序走。"
            
            jump ch1_scene5

        # 分支C：摊牌施压
        label ch1_scene4_branch_C:
            show image "gui/paper_crumpled.png" at right with dissolve
            shen_si "（拿起桌上揉皱的诊断证明，在手里轻轻拍打）我已经知道这是假的。省医那边我核实过了。"
            
            show lin_zixuan_terrified with dissolve
            lin_zixuan "我……"
            
            shen_si "（抬手制止他）但我没上报。给你最后一次机会。"
            
            lin_zixuan "（声音颤抖）沈老师……"
            
            shen_si "（站起身，指着电脑）现在，要么你跟我说实话，论文到底能不能改好？"
            shen_si "要么……我现在就打电话给学生处。"
            
            lin_zixuan "（突然崩溃，蹲在地上哭）能！我能改！我只是……只是不知道怎么改……"
            
            show shen_si_sigh with dissolve
            shen_si "（叹了口气，递给他纸巾）起来吧。我给你找个人辅导。"
            
            jump ch1_scene5

    # ============================================================
    # 场景5：办公室 · 第二天上午
    # ============================================================
    label ch1_scene5:
        scene bg_office with fade
        
        narrator "沈思的办公室，张导师坐在对面，手里拿着林子轩的论文。"
        
        show zhang_professor with dissolve
        zhang_professor "（摇头）数据分析确实有问题，但……（看向沈思）你确定要保他？"
        
        shen_si "（坚定）他本质不坏，就是走投无路了。而且论文框架很完整，只是方法用错了。"
        
        zhang_professor "（沉默片刻）……好吧。我今天下午带他把数据分析过一遍。"
        zhang_professor "但丑话说在前头，要是两周后还达不到要求，我不会松口。"
        
        shen_si "（点头）谢谢张老师。"

        # 选择分支6
        menu ch1_choice_6:
            "立刻给林子轩打电话：'子轩，张老师同意给你机会了，下午去实验室！'" :  # 第一时间通知
                $ ch1_choice_record.append("ch1_6_A")
                $ empathy += 1
                $ ch1_empathy_delta += 1
                jump ch1_scene5_branch_A
            
            "先给心理中心打电话：'我这里有个学生，状态很不稳定，需要……'" :  # 优先关注心理
                $ ch1_choice_record.append("ch1_6_B")
                $ empathy += 1
                $ ch1_empathy_delta += 1
                jump ch1_scene5_branch_B
            
            "坐在座位上，闭上眼睛深呼吸——终于争取到了机会，但接下来的路还很长" :  # 短暂休整
                $ ch1_choice_record.append("ch1_6_C")
                $ resilience += 1
                $ ch1_resilience_delta += 1
                jump ch1_scene5_branch_C

        # 分支A：第一时间通知
        label ch1_scene5_branch_A:
            narrator "张导师刚走，沈思立刻拿出手机。"
            
            shen_si "（打电话）子轩，是我。张老师同意给你机会了，今天下午三点去他实验室！"
            
            narrator "电话那头沉默了几秒，然后传来林子轩带着哭腔的声音。"
            
            observe_text "【林子轩】……谢谢沈老师……"
            
            shen_si "（语气温和）别谢我，这是你自己争取的。好好把握。"
            
            jump ch1_epilogue

        # 分支B：关注心理
        label ch1_scene5_branch_B:
            shen_si "（拿起电话，拨通心理中心）你好，我是研究生院的沈思。"
            shen_si "我这里有个学生，林子轩，最近状态很不稳定，有过极端言论……"
            
            narrator "她详细说明了情况，然后挂断电话。接着才给林子轩发消息。"
            
            observe_text "【消息】子轩，张老师同意下午带你改论文了。另外，心理中心那边我也打了招呼，有空可以去聊聊。"
            
            jump ch1_epilogue

        # 分支C：短暂休整
        label ch1_scene5_branch_C:
            show shen_si_tired with dissolve
            shen_si "（疲惫地靠在椅背上，闭上眼睛）"
            
            narrator "办公室里很安静，只有空调的轻微嗡嗡声。"
            narrator "她在脑海里梳理着：诊断证明造假——需要内部记录；论文修改——张导师已同意指导；"
            narrator "学生心理状态——需要跟进；就业压力——可能需要联系学院就业办。"
            
            shen_si "（睁开眼睛，拿起手机）子轩，张老师同意下午三点带你改论文。准备好最新版。"
            
            jump ch1_epilogue

    # ============================================================
    # 尾声：两个月后
    # ============================================================
    label ch1_epilogue:
        scene black with fade
        pause 1
        
        scene bg_office_sunny with fade
        
        narrator "两个月后，沈思收到了一张明信片。"
        narrator "正面是乡间小路，背面只有几个字："
        
        observe_text "「沈老师，谢谢您。九月见。」"
        
        show shen_si_smiling with dissolve
        shen_si "（微笑着将明信片收进抽屉）"
        
        narrator "窗外，广州的阳光正盛。"

        # 数值变化汇总
        $ chapter1_completed = True
        $ ch1_linzixuan_outcome = "延期毕业，正在修改论文"
        
        # 根据选择记录追加额外数值
        if "ch1_2_A" in ch1_choice_record or "ch1_3_A" in ch1_choice_record:
            $ integrity += 2
            $ ch1_integrity_delta += 2
        if "ch1_5_A" in ch1_choice_record:
            $ insight += 2
            $ ch1_insight_delta += 2
        if ch1_helped_student:
            $ empathy += 2
            $ ch1_empathy_delta += 2
        if "ch1_6_C" in ch1_choice_record:
            $ resilience += 1
            $ ch1_resilience_delta += 1
        
        # 显示本章结果
        show text "【第一章 论文风云 · 完】" with dissolve
        pause 2
        
        show text "本章数值变化：" with dissolve
        pause 1
        
        show text "正直值: +%d | 洞察值: +%d | 同理心: +%d | 韧性值: +%d" % (
            ch1_integrity_delta, ch1_insight_delta, ch1_empathy_delta, ch1_resilience_delta
        ) with dissolve
        pause 3
        
        hide text with dissolve
        
        # 进入下一章
        $ chapter = 2
        jump chapter2_start

    return
