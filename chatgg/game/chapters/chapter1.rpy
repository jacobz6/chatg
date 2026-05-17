# -*- coding: utf-8 -*-
# ============================================================
# chapter1.rpy — 第一章：论文风云
# ============================================================

label chapter1_start:
    scene black with fade
    narrator "2026年5月，南方一线城市。"
    narrator "五月的广州，潮湿的空气里弥漫着芒果花的香气。"
    narrator "研究生院办公室的百叶窗半开着，晨光在浅灰色的办公桌上投下细密的光条纹。"
    narrator "墙上挂着'明德博学，求是创新'的院训，旁边是一排整齐的文件柜。"

    scene bg office with dissolve
    narrator "沈思比平时早到了二十分钟。"
    narrator "作为研究生院秘书，她早已习惯了在正式上班前先理一理今天的工作。"
    narrator "这几天是毕业论文提交的冲刺期，电话和邮件都会比平时多出三四倍。"

    narrator "她给自己泡了杯茶，打开电脑，桌面上的待办事项清单密密麻麻。"

    scene bg office with dissolve
    narrator "「咚咚咚——」"
    narrator "有人在敲门，节奏有点犹豫，不像平时那些雷厉风行的学生干部。"

    show lin_zixuan:
        xalign 0.5
        yalign 0.3

    narrator "林子轩推门进来，手里攥着一个牛皮纸档案袋。"
    narrator "他穿着格子衬衫，洗得有些发白，袖口微微卷起。"
    narrator "沈思注意到他的手指在档案袋边缘无意识地摩挲着，指节微微发白。"

    lin_zixuan "沈老师，早上好……打扰您了。"

    narrator "他站在门口，没有像有些学生那样直接闯进来沙发上坐下。"

    shen_si "请坐吧，什么事？"

    lin_zixuan "沈老师，我……我有件事想跟您商量。"

    shen_si "别紧张，慢慢说。"

    lin_zixuan "是这样的，我的论文……提交超期了。"

    shen_si "超期？子轩，你知道今年论文提交的截止日期是5月20号，今天已经17号了……"

    lin_zixuan "我知道，我知道的，沈老师。（他的语速加快了）但我真的有特殊情况……"

    shen_si "什么特殊情况？能说说吗？"

    menu ch1_scene1_choice1:
        "按规定，超期申请需要院长审批，而且时间这么紧，恐怕很难……":
            jump ch1_scene1a
        "认真地看着他，等他继续说下去（耐心倾听）":
            jump ch1_scene1b
        "你应该知道这个时间点很敏感，所有流程都要按规矩来。":
            jump ch1_scene1c

label ch1_scene1b:
    narrator "沈思没有立刻打断他，而是将手边的工作推到一旁，认真地看向他。"
    narrator "这种不带评判的注视让林子轩紧绷的肩膀微微松了松。"

    lin_zixuan "沈老师，其实我……我签了一家深圳的公司，年薪三十五万。"
    lin_zixuan "他们要求6月1号之前拿到双证，否则offer就作废了。"

    narrator "他说到'三十五万'的时候，声音里有一丝难以掩饰的骄傲。"

    shen_si "这是好事啊。"

    lin_zixuan "是好消息，但……（他的眼神黯淡下去）我导师老张上周找我谈话，说我的论文数据有个实验组存在统计问题，需要补充验证。"

    shen_si "所以你现在的论文状态是……"

    lin_zixuan "（低下头）还在修改。我通宵改了一周了，真的……沈老师，我快撑不住了。"

    $ ch1_choice_record.append("scene1_patient_listening")

    jump ch1_scene1_after

label ch1_scene1a:
    narrator "沈思皱了皱眉。"

    shen_si "按规定，超期申请需要院长审批，而且时间这么紧，恐怕很难……"

    lin_zixuan "但是沈老师，我真的……"

    $ ch1_choice_record.append("scene1_direct_difficult")

    jump ch1_scene1_after

label ch1_scene1c:
    narrator "沈思的语气变得更严肃了一些。"

    shen_si "你应该知道这个时间点很敏感，所有流程都要按规矩来。"

    lin_zixuan "我知道……但是沈老师……"

    $ ch1_choice_record.append("scene1_warn_serious")

    jump ch1_scene1_after

label ch1_scene1_after:
    narrator "就在这时，林子轩像是下定了什么决心似的，打开了手里的档案袋，从里面抽出一张纸，放在沈思面前。"

    lin_zixuan "沈老师，这是我上周的急诊病历和住院证明。我——我急性阑尾炎发作，在省人民医院做了手术，住院一周。"

    narrator "沈思拿起那张'广东省人民医院'的诊断证明，上面盖着红彤彤的公章。"
    narrator "纸张的质地很好，印刷也很清晰。诊断结果写着'急性化脓性阑尾炎'，落款日期是5月8日。"

    shen_si "手术……阑尾切除术？"

    lin_zixuan "（点头如捣蒜）对对对，就是这个。"

    shen_si "（沉默了几秒）子轩，你说你在省人民医院做的手术？"

    lin_zixuan "（眼神闪烁了一下）对……对啊，有什么问题吗？"

    menu ch1_scene2_choice1:
        "省人民医院急诊科在5月8日那天启动了新系统，诊断证明的格式不是这样的。":
            jump ch1_scene2a
        "这样吧，我把这份材料提交给学院核实一下，你先回去等通知。":
            jump ch1_scene2b
        "我注意到了几个细节，但先不下结论，继续追问。":
            jump ch1_scene2c

label ch1_scene2a:
    narrator "沈思皱了皱眉，决定直接戳穿。"

    shen_si "省人民医院急诊科在5月8日那天启动了新系统，诊断证明的格式不是这样的。"

    lin_zixuan "（脸色突变）什……什么？"

    $ ch1_choice_record.append("scene2_expose_immediately")
    $ insight += 1

    jump ch1_scene2_after

label ch1_scene2b:
    narrator "沈思决定先稳住局面。"

    shen_si "这样吧，我把这份材料提交给学院核实一下，你先回去等通知。"

    lin_zixuan "好的，谢谢沈老师！"

    $ ch1_choice_record.append("scene2_submit_verify")

    jump ch1_scene2_after

label ch1_scene2c:
    narrator "沈思没有立刻戳穿。她在行政岗位干了三年，见过形形色色的'特殊情况'。"
    narrator "她不动声色地将诊断证明放回桌上，手指'不经意'地点了点纸张左下角。"

    shen_si "子轩啊，我理解你的难处。这样，这份材料我先收下，按照流程需要提交给学院核实。"

    lin_zixuan "（眼中闪过一丝惊喜）真的吗？沈老师，太谢谢您了！"

    shen_si "不过——病历原件你带了吗？我需要留存一份复印件。"

    lin_zixuan "原件……在，在家里，我回去拍个照片发给您？"

    shen_si "好的。不过子轩，学院审核这种特殊申请，会调取医院的原始病历系统记录。你方便授权我们核实吗？"

    narrator "林子轩的喉结滚动了一下。"

    lin_zixuan "这……这需要吗？"

    shen_si "这是规定。为了保护你的权益，也为了保护我们双方。"

    $ ch1_choice_record.append("scene2_note_clues")
    $ insight += 1

    jump ch1_scene2_after

label ch1_scene2_after:
    narrator "她起身走到饮水机旁，给自己的茶杯续了点水。"
    narrator "当她转过身时，看到的是一个正在努力控制表情的年轻学生。"

    lin_zixuan "（站起来，声音有些干涩）沈老师，我……我明白了。我回去考虑一下。"

    shen_si "好，你先回去。"

    hide lin_zixuan

    scene black with fade

    narrator "【场景2：核实 · 当天下午】"
    narrator "午休时间，办公室的其他同事都去吃饭或者午睡了。"
    narrator "沈思一个人坐在工位上，面前的电脑上开着医院的电子票据查验系统。"

    scene bg office with dissolve
    narrator "她用查验系统扫了一遍林子轩提供的'诊断证明'上的票据编号。"
    narrator "屏幕上弹出一行字：'该票据不存在'。"
    narrator "果然。"

    narrator "她又打开了另一个窗口——省人民医院5月8日那天的电子病历系统公告。"
    narrator "那天急诊科系统更新，暂停了三个小时的门诊挂号。"

    narrator "沈思又看了看手里的这张纸。不说别的，光是纸张的克数就不对——真正的医院诊断证明用的是特制的带水印纸。"

    narrator "她闭上眼睛，靠在椅背上。脑海里浮现出林子轩早上那双布满血丝的眼睛。"

    narrator "这孩子……是真急了。"

    scene bg office with dissolve
    narrator "就在这时，办公室的门被推开了。进来的是一个四十多岁的中年女人，头发一丝不苟地盘在脑后，金丝眼镜后面的眼神透着精明。"

    show wang_director:
        xalign 0.5
        yalign 0.3

    wang_director "小沈，听说有个叫林子轩的学生找你申请超期？"

    shen_si "（站起身）王主任，是的。他自称急性阑尾炎手术，需要申请论文延期提交。"

    wang_director "（眉头皱了起来）又来一个。每年这时候都有人想钻空子。你怎么看？"

    menu ch1_scene3_choice1:
        "我核实过了，诊断证明存在问题。我建议拒绝他的申请。":
            jump ch1_scene3a
        "还在核实中，目前不确定。主任您看怎么处理？":
            jump ch1_scene3b
        "我觉得应该再给学生一个机会，毕竟……":
            jump ch1_scene3c

label ch1_scene3a:
    narrator "沈思深吸一口气。"

    shen_si "王主任，我中午用医院的票据系统查验过了，这张诊断证明的编号不存在。"

    shen_si "而且省人民医院5月8日当天急诊系统更新，诊断证明的格式和现在这张也不一样。"

    narrator "她把打印出来的查验结果递给王主任。"

    wang_director "（接过纸，仔细看了看，脸色沉下来）伪造病历？"

    shen_si "从目前核实的情况来看，有很大嫌疑。"

    wang_director "（将纸拍在桌上）这些学生，真是越来越过分了！"

    narrator "王主任脸色阴沉。"

    $ ch1_choice_record.append("scene3_report_truth")
    $ ch1_reported_fake = True
    $ integrity += 1

    jump ch1_scene3_after

label ch1_scene3b:
    narrator "沈思谨慎地回答。"

    shen_si "还在核实中，目前不确定。主任您看怎么处理？"

    wang_director "这种事还要我教你？按规定来！"

    $ ch1_choice_record.append("scene3_ask_director")

    jump ch1_scene3_after

label ch1_scene3c:
    narrator "沈思试图为学生说话。"

    shen_si "我觉得应该再给学生一个机会，毕竟……"

    wang_director "（打断她）小沈，你心软我知道。但规矩就是规矩！"

    $ ch1_choice_record.append("scene3_plead_student")

    jump ch1_scene3_after

label ch1_scene3_after:
    hide wang_director

    scene bg office with dissolve
    narrator "王主任转身离开了。沈思重新坐回椅子上，感到一阵说不清的疲惫。"

    narrator "【场景3：食堂 · 傍晚】"
    narrator "傍晚六点半，研究生院食堂二楼。"
    narrator "她刚夹起一块叉烧，手机屏幕亮了。"

    narrator "是同事刘姐发来的消息。"

    liu_jie "沈思，听说今天有个学生找你办超期？"
    liu_jie "小心点，今年就业形势不好，这种事情特别多。"

    shen_si "……知道了，谢谢刘姐提醒。"

    narrator "她放下手机，对着盘子里已经凉了的饭菜，突然没了胃口。"

    narrator "「沈老师？」"

    show wang_yuqin:
        xalign 0.5
        yalign 0.3

    narrator "一个清亮的声音从背后传来。沈思回头，看到一个扎着马尾辫的女生正端着餐盘站在旁边。"

    wang_yuqin "沈老师好！我是林子轩的室友，王雨晴。"

    shen_si "（努力挤出一个微笑）哦，你好你好，坐吧。"

    wang_yuqin "（压低声音）沈老师，我想跟您说点事……关于子轩的。"

    shen_si "他怎么了？"

    wang_yuqin "（叹气）他昨天在宿舍说了一些奇怪的话，什么'活着有什么意思''对不起父母的培养'之类的。"

    wang_yuqin "沈老师，我怕他……"

    shen_si "那你们有没有告诉辅导员？"

    wang_yuqin "沈老师，您也知道，研究生和本科生不一样。导师责任制，辅导员根本管不到。"

    wang_yuqin "沈老师，我知道子轩那个申请可能有点问题。但是……他真的是个好人，就是一时糊涂。"

    menu ch1_scene4_choice1:
        "雨晴，我理解你的担心。但是规矩就是规矩，不能因为同情就破坏。":
            jump ch1_scene4a
        "谢谢你告诉我这些。我会再想想办法，但不能保证什么。":
            jump ch1_scene4b
        "他现在在哪里？我想亲自和他谈谈。":
            jump ch1_scene4c

label ch1_scene4a:
    narrator "沈思坚持原则。"

    shen_si "雨晴，我理解你的担心。但是规矩就是规矩，不能因为同情就破坏。"

    wang_yuqin "（失望）好吧……沈老师，那打扰您了。"

    $ ch1_choice_record.append("scene4_insist_rule")

    jump ch1_chapter1_ending_a

label ch1_scene4b:
    narrator "沈思留有余地。"

    shen_si "谢谢你告诉我这些。我会再想想办法，但不能保证什么。"

    wang_yuqin "好的，谢谢沈老师！"

    $ ch1_choice_record.append("scene4_keep余地")

    jump ch1_chapter1_ending_a

label ch1_scene4c:
    narrator "沈思做出了一个连自己都意外的决定。"

    shen_si "他现在在哪里？我想亲自和他谈谈。"

    wang_yuqin "（愣了一下，随即眼眶微红）真的吗？沈老师，谢谢您！"

    wang_yuqin "他在……他应该在宿舍。我们宿舍在东区学7栋，404室。"

    shen_si "好，我现在就去。"

    $ ch1_choice_record.append("scene4_visit_dorm")
    $ empathy += 1

    hide wang_yuqin

    scene black with fade

    narrator "【场景4：宿舍楼 · 夜】"
    narrator "东区学7栋是一栋老旧的六层宿舍楼，楼道里的声控灯忽明忽暗。"
    narrator "404室在三楼走廊尽头，门上贴着褪色的'文明宿舍'标签。"

    scene bg corridor with dissolve
    narrator "沈思站在门口，听到里面传来键盘敲击的声音，噼里啪啦的。"

    narrator "她敲了敲门。"

    lin_zixuan "（画外音）谁啊？"

    shen_si "子轩，是我，研究生院的沈老师。"

    narrator "门内沉默了几秒。然后是慌乱的脚步声，有人把什么东西碰倒了。"

    show lin_zixuan:
        xalign 0.5
        yalign 0.3

    narrator "门开了。"
    narrator "林子轩站在门口，穿着皱巴巴的T恤，眼镜歪在鼻梁上，头发像鸟窝一样乱。"
    narrator "他的眼睛比早上更红了，布满血丝。"

    lin_zixuan "（惊讶）沈……沈老师？您怎么来了？"

    shen_si "路过你们宿舍楼，想着你身体还在恢复，就顺便上来看看。"

    narrator "林子轩犹豫了一下，侧身让开了门。"

    narrator "宿舍是标准的四人间，但只有他一个人住。空荡荡的房间里，只有角落的电脑屏幕亮着。"

    lin_zixuan "（手忙脚乱地收拾桌上的杂物）沈老师您坐，我这儿有点乱……"

    shen_si "别忙了，过来坐吧。"

    narrator "两人相对而坐。沈思的目光落在桌上那张被揉皱又展开的诊断证明上。"

    shen_si "子轩，这张诊断证明……是假的吧？"

    narrator "林子轩的身体僵住了。"

    lin_zixuan "（声音发抖）沈老师，我……"

    shen_si "（叹气）省人民医院的票据查验系统查不到这个编号。"

    shen_si "我没有第一时间揭穿你，是想给你一个主动承认的机会。"

    lin_zixuan "（突然站起来）沈老师，对不起！我……我是被逼的！我真的没办法！"

    narrator "他的眼泪突然就流了下来。"

    lin_zixuan "我爸妈是农民，供我读书已经倾家荡产了……我签了深圳那家公司，三十五万……"

    lin_zixuan "可是论文出了问题，老张又不让我过……我找不到别的办法了……"

    narrator "沈思沉默地看着眼前这个崩溃的年轻人。"

    menu ch1_scene5_choice1:
        "子轩，哭完了擦擦眼泪。伪造病历这件事，我会按照规定上报。":
            jump ch1_scene5a
        "我理解你的处境。但这件事不能再继续了，你要么老老实实补论文，要么……放弃这次毕业。":
            jump ch1_scene5b
        "我帮你想想办法。但你要答应我，从现在开始，不许再有任何侥幸心理。":
            jump ch1_scene5c

label ch1_scene5a:
    narrator "沈思选择上报。"

    shen_si "子轩，哭完了擦擦眼泪。伪造病历这件事，我会按照规定上报。"

    lin_zixuan "（绝望）不要！沈老师，求求您！"

    $ ch1_choice_record.append("scene5_report")

    jump ch1_scene5_after

label ch1_scene5b:
    narrator "沈思给了他一条路。"

    shen_si "擦擦眼泪。"

    narrator "林子轩接过纸巾，胡乱擦了擦脸。"

    shen_si "子轩，我理解你的处境。但是——伪造病历，这件事本身就是错的。"

    shen_si "现在摆在你面前的路只有两条。"

    shen_si "第一条，老老实实补实验、补论文。哪怕这次延毕，至少你还有学位。"

    shen_si "放弃这次答辩，回去找工作。深圳那家公司如果真的看重你，应该会等你。"

    shen_si "你爸妈供你读书，是希望你有个好前途，不是希望你为了一个offer把自己逼死。"

    lin_zixuan "（愣住）可是……可是我爸妈……"

    shen_si "从现在开始，不许再动任何侥幸的念头。"

    $ ch1_choice_record.append("scene5_give_path")
    $ empathy += 1
    $ ch1_helped_student = True

    jump ch1_scene5_after

label ch1_scene5c:
    narrator "沈思决定帮他。"

    shen_si "我帮你想想办法。但你要答应我，从现在开始，不许再有任何侥幸心理。"

    lin_zixuan "（点头如捣蒜）我答应您！谢谢沈老师！"

    $ ch1_choice_record.append("scene5_help_him")
    $ empathy += 1

    jump ch1_scene5_after

label ch1_scene5_after:
    scene black with fade

    narrator "【场景5：办公室 · 第二天上午】"
    narrator "沈思的办公室里，阳光依然明媚。"
    narrator "她面前的桌上摆着一份手写的清单——林子轩的论文进度分析。"

    scene bg office with dissolve
    narrator "出乎意料的是，这孩子的论文其实已经完成了90%。只剩下最后的数据验证和结论部分的润色。"

    narrator "就在这时，她的手机响了。来电显示：陈明德教授。"

    narrator "陈教授是学院的副院长，也是研究生培养方面的负责人。这么早打来电话，让沈思有种不祥的预感。"

    chen_professor "小沈啊，我听说有个叫林子轩的学生找你办超期申请？"

    shen_si "（接起电话）陈院长您好……"

    chen_professor "（画外音，态度严厉）谁让你去核实的？这种申请本来就应该直接驳回！"

    narrator "电话挂断了。沈思盯着手机屏幕，一股委屈和愤怒同时涌上心头。"

    scene bg office with dissolve
    narrator "就在这时，办公室的门被推开了。进来的是一个五十多岁的男人，头发花白，穿着老式的polo衫。"

    show zhang_professor:
        xalign 0.5
        yalign 0.3

    zhang_professor "沈老师是吧？我是林子轩的导师，老张。"

    shen_si "张教授您好，请坐。"

    zhang_professor "（坐下，叹了口气）小沈啊，子轩的事我听说了。那孩子找我谈过几次。"

    shen_si "张教授，那他现在论文的进度是……？"

    zhang_professor "（摇头）还差得远呢。按照他现在这个状态，再给三个月都够呛。"

    narrator "沈思的心彻底沉了下去。"

    menu ch1_scene6_choice1:
        "把林子轩的进度清单给张教授看，说明实际情况。":
            jump ch1_scene6a
        "问张教授能否给林子轩一些灵活的处理方案。":
            jump ch1_scene6b
        "沉默。心里已经有了决定。":
            jump ch1_scene6c

label ch1_scene6a:
    narrator "沈思从桌上拿起那份清单，递给张教授。"

    shen_si "张教授，您看看这个。这是林子轩的论文进度分析。"

    narrator "张教授接过清单，眯着眼睛看了半天，眉头渐渐皱了起来。"

    zhang_professor "（喃喃自语）完成90%了？怎么可能……"

    shen_si "除了数据验证和结论部分，基本框架都有了。如果有人指导他集中精力，三天……"

    zhang_professor "（放下清单）数据验证那块确实有问题，但不是不能做。是我之前太忙……"

    narrator "他的语气里有了一丝愧疚。"

    zhang_professor "这样吧。我今天下午把子轩叫到实验室，带他过一遍数据问题。"

    zhang_professor "明天晚上之前把论文交给我，我给他走加急送审。"

    $ ch1_choice_record.append("scene6_show_progress")
    $ integrity += 1

    jump ch1_scene6_after

label ch1_scene6b:
    narrator "沈思试图寻求妥协。"

    shen_si "张教授，能不能给这孩子一个机会？他真的很不容易……"

    zhang_professor "沈老师，我理解你的心情。但规矩就是规矩。"

    $ ch1_choice_record.append("scene6_seek_compromise")

    jump ch1_scene6_after

label ch1_scene6c:
    narrator "沈思沉默了。她已经决定不了什么了。"

    $ ch1_choice_record.append("scene6_silent")

    jump ch1_scene6_after

label ch1_scene6_after:
    hide zhang_professor

    scene black with fade

    narrator "【场景6：一个月后 · 六月】"
    narrator "一个月后的广州，炎热的夏季正式开始。"
    narrator "研究生院的毕业典礼在庄严的礼堂里举行，毕业生们穿着黑色的学位服。"

    scene bg office with dissolve
    narrator "沈思站在礼堂最后方，手里捧着一束向日葵。"

    narrator "人群里，她看到了一个熟悉的身影。林子轩穿着学位服站在队伍中间，脸上带着如释重负的笑容。"

    narrator "林子轩的父亲——一个皮肤黝黑、双手粗糙的庄稼人——正在用乡音浓重的普通话和旁边的家长攀谈："

    narrator "'我儿子，研究生！'"

    narrator "沈思远远地看着这一幕，心里涌起一阵暖流。"

    narrator "她成功地帮助了一个迷途的年轻人。在规则和人性的天平上，她找到了平衡点。"

    narrator "——"

    narrator "但就在这时，她的手机震动了。"

    narrator "是王雨晴发来的消息。"

    narrator "王雨晴：沈老师，子轩出了点事，您方便吗？"

    narrator "沈思：怎么了？"

    narrator "王雨晴：深圳那家公司……取消了他的offer。"

    narrator "沈思的心猛地揪紧了。"

    narrator "沈思：他现在怎么样？"

    narrator "王雨晴：不知道……他把我们所有人的联系方式都拉黑了。"

    narrator "沈思冲出礼堂，拦了一辆出租车，往东区学7栋赶去。"

    scene black with fade

    narrator "【场景7：宿舍楼 · 当天下午】"
    narrator "404室的门紧闭着，从门缝里透不出一丝光线。"

    scene bg corridor with dissolve
    narrator "沈思用力敲门，没有回应。"
    narrator "她掏出备用钥匙——打开了门。"

    narrator "宿舍里一片昏暗，窗帘拉得严严实实。"

    narrator "而林子轩——"

    narrator "他蜷缩在床上，背对着门，一动不动。"

    shen_si "（轻声）子轩？"

    narrator "没有回应。"

    shen_si "（走近）子轩，是我，沈老师。"

    show lin_zixuan:
        xalign 0.5
        yalign 0.3

    narrator "林子轩缓缓转过身来。他的脸色苍白如纸，嘴唇干裂，眼窝深陷。"

    lin_zixuan "（声音嘶哑）沈老师……你来了。"

    shen_si "你吓死我了。你怎么样？为什么要拉黑所有人？"

    lin_zixuan "（苦笑）沈老师，我没脸见人。我连一个offer都保不住。活着还有什么意义？"

    shen_si "（急切）子轩，工作没了可以再找，延毕了可以再读。但你要是出了什么事，你爸妈怎么办？"

    lin_zixuan "（打断她）沈老师，您不用安慰我。我都懂。可是我……我真的撑不下去了。"

    narrator "他从枕头下面摸出一个东西——是一把美工刀。"

    lin_zixuan "（眼神决绝）谢谢您这段时间对我的帮助。您是个好人。但我……"

    menu ch1_scene7_choice1:
        "立刻冲上去夺刀！":
            jump ch1_scene7a
        "子轩，你先把刀放下，我们谈谈。":
            jump ch1_scene7b
        "你要是这样做，你爸妈怎么办？":
            jump ch1_scene7c

label ch1_scene7a:
    narrator "沈思毫不犹豫地冲了上去！"

    narrator "她一把抓住林子轩的手腕，用力将美工刀打落在地！"

    lin_zixuan "（惊呼）沈老师！"

    shen_si "你疯了吗！"

    $ ch1_choice_record.append("scene7_grab_knife")
    $ resilience += 1

    jump ch1_scene7_after

label ch1_scene7b:
    narrator "沈思强迫自己冷静下来。她慢慢蹲下身，让自己的视线和林子轩平齐。"

    shen_si "子轩，你先听我说。"

    lin_zixuan "（手握着刀，没有动）"

    shen_si "你做的决定，我不评判。但是……能不能给我五分钟？"

    lin_zixuan "……五分钟。"

    shen_si "（松了一口气）谢谢。"

    shen_si "子轩，你知道吗，我也是农村出来的。"

    narrator "林子轩的眼神微微动了一下。"

    shen_si "我老家在湖南一个很偏的县城。我妈当年说，'闺女，妈这辈子最后悔的事，就是当年没勇气走出那个村子。'"

    shen_si "我后来考上了研究生，来了广州，留在这里工作。我妈去年走了，走之前跟我说，她这辈子最骄傲的事，就是培养了一个研究生女儿。"

    shen_si "子轩，你爸妈供你读书，不是为了让你拿高薪offer给他们长脸。是因为他们希望你有机会看看更大的世界。"

    lin_zixuan "（嘴唇微微颤抖）"

    shen_si "你现在遇到的挫折，不是终点，是一个让你变得更强大的机会。"

    narrator "林子轩低着头，手里的刀渐渐松了。他开始颤抖，然后是压抑的哭声。"

    lin_zixuan "（哽咽）沈老师……我好累……"

    shen_si "（轻轻抱住他）累了就哭出来。哭完了，我们一起想办法。"

    $ ch1_choice_record.append("scene7_calm_down")
    $ ch1_student_suicide_attempted = True
    $ empathy += 1
    $ resilience += 1

    jump ch1_scene7_after

label ch1_scene7c:
    narrator "沈思试图打感情牌。"

    shen_si "你要是这样做，你爸妈怎么办？你想过他们吗？"

    lin_zixuan "（愣了一下）爸妈……"

    narrator "但美工刀还在他手里。"

    $ ch1_choice_record.append("scene7_emotional_card")

    jump ch1_scene7_after

label ch1_scene7_after:
    scene black with fade

    narrator "【尾声：两周后】"
    narrator "两周后，沈思收到了一封信。信封上是林子轩的字迹，工整而有力。"

    scene bg office with dissolve
    narrator "「沈老师：」"
    narrator "「谢谢您那天的当头棒喝。我现在在医院接受心理治疗，情况稳定了很多。」"
    narrator "「深圳那家公司，我打电话去沟通了。他们说如果我明年拿到学位，可以重新考虑录用。」"
    narrator "「我爸前几天来看我了。他没有骂我，只是摸了摸我的头，说'回家吧，爸养你'。」"
    narrator "「沈老师，谢谢您救了我一命。我会好好活下去的。」"
    narrator "「林子轩」"
    narrator "「2026年6月15日」"

    narrator "沈思放下信，望向窗外。五月的阳光依然明媚，芒果花的香气从窗外飘进来。"

    narrator "她觉得自己做了一个正确的决定。虽然过程曲折，但至少，她没有让一个年轻的生命就此消逝。"

    narrator "这就够了吧？"

    narrator "——"

    narrator "每当夜深人静的时候，她总是忍不住想："
    narrator "如果当时她没有坚持原则，直接批准了林子轩的超期申请……结果会不会不一样？"

    narrator "这个问题没有答案。"
    narrator "也许永远都不会有。"

    $ chapter1_completed = True
    $ ch1_linzixuan_outcome = "康复中"

    scene black with fade

    narrator "【第一章 · 完】"
    narrator "本章数值变化："
    narrator "integrity: [integrity] | insight: [insight] | empathy: [empathy] | resilience: [resilience]"
    narrator "学生结局：林子轩 — 康复中"
    narrator "关键选择记录：[len(ch1_choice_record)]项"

    return

label ch1_chapter1_ending_a:
    scene black with fade
    narrator "【第一章 · 完】"
    narrator "本章数值变化："
    narrator "integrity: [integrity] | insight: [insight] | empathy: [empathy] | resilience: [resilience]"
    narrator "学生结局：林子轩 — [ch1_linzixuan_outcome]"
    narrator "关键选择记录：[len(ch1_choice_record)]项"

    $ chapter1_completed = True

    return
