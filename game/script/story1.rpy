label story1:

    play music "audio/main.mp3"
    scene beach_night

        # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
        # “eileen happy.png”的文件来将其替换掉。

        # 此处显示各行对话。
    e "开始！！"
    $ live2dsupport = renpy.has_live2d()
    if live2dsupport:
        show Mark m01 m02 m03 m04 m05 m06 with dissolve
    else:
        show hiyori m01 m02 m03 m04 m05 m06 m07 m08 m09 m10 with dissolve
    e "Ren'Py现在支持并行显示多行对话了。" (multiple=2)
    l "\n该死的！我等这个功能好多年了。" (multiple=2)


    hide Mark
    hide hiyori
    show Haru g_idle g_m01 g_m02 g_m03 g_m04 g_m05 g_m06 g_m07 g_m08 g_m09 g_m10 g_m11 g_m12 g_m13 g_m14 g_m15 g_m16 g_m17 g_m18 g_m19 g_m20 g_m21 g_m22 g_m23 g_m24 g_m25 g_m26 g_idle with dissolve
    e "呐～，这边这样就可以了吧？"
    hide Haru
    show Natori mtn_00 mtn_01 mtn_02 mtn_03 mtn_04 mtn_05 mtn_06 mtn_07 with dissolve
    e "呐～，这边这样就可以了吧？"
    hide Natori
    show Mark m01 m02 m03 m04 m05 m06 with dissolve
    e "呐～，这边这样就可以了吧？"
    hide Mark






    menu nexxt_button:
        "name"
        "是":
            pass

        "否":
            pass
            #block of code to run
    hide g_s with dissolve
    show g_s at left with Ds
    e "呐～，这边这样就可以了吧？"
    show m_s at right with Ds
    l "嗯，这样就行了。谢谢你来帮我照顾香草"
    show g_b_s at left with Ds
    e "哈哈，不用谢不用谢～。反倒是我借着这个机会从老爹那里逃出来了，"
    show m_b_s at right with Ds
    l "嘛～，西欧罗你也真是的……要是被老板听到了，他又要发火了哦"
    show g_s at left with Ds
    e "喂喂～，别这么说嘛～"
    show m_s at right with Ds
    l "呵呵，玩笑而已啦～"
    show g_p at left with Ds
    e "这种玩笑对心脏可不好啊"
    show m_p at right with Ds
    l "呐，……你看那个是什么啊"
    show g_p at left with Ds
    e "嗯，哪个？"

    l "是什么呢……？"

    e "……啊！"

    l "嘛，反正八成就是个兔子什么的吧？　别管啦～"

    e "真是吓我一跳……"

    l "吓了一跳啊……嘛，我觉得大概又是什么虫子在偷吃香草了吧……"

    e "真的出大事了啊。那里倒了一个人……"

    l "哈？"

    e "有个男人倒在那里……"

    l "你说什么！？"

    e "快，来这边……"

    l "这，这该不会就是死在路旁的人吧！　大事不妙啊！　该怎么办"

    e "所以刚才我不是说了嘛……"

    l "总之先把人……得先神父叫来！"

    "唔……水，……水……"

    e "啊，等下。这个人的身体似乎非常虚弱……先给他水吧"

    l "哦，哦！"

    e "然后，拿点金缕梅的叶子来……"
    e """

    燕子去了，有再来的时候；

    杨柳枯了，有再青的时候；Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。
    Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。Ren'Py现在支持并行显示多行对话了。

    桃花谢了，有再开的时候。

    但是，聪明的，你告诉我，我们的日子为什么一去不复返呢？

    ——是有人偷了他们罢：

    那是谁？又藏在何处呢？

    是他们自己逃走了罢：现在又到了哪里呢？

    我不知道他们给了我多少日子；

    但我的手确乎是渐渐空虚了。

    在默默里算着，八千多日子已经从我手中溜去；

    像针尖上一滴水滴在大海里，

    我的日子滴在时间的流里，

    没有声音，也没有影子。

    我不禁头涔涔而泪潸潸了。

    去的尽管去了，来的尽管来着；

    去来的中间，又怎样地匆匆呢？

    早上我起来的时候，小屋里射进两三方斜斜的太阳。

    太阳他有脚啊，轻轻悄悄地挪移了；

    我也茫茫然跟着旋转。

    于是——洗手的时候，日子从水盆里过去；

    吃饭的时候，日子从饭碗里过去；

    默默时，便从凝然的双眼前过去。

    我觉察他去的匆匆了，

    伸出手遮挽时，他又从遮挽着的手边过去，

    天黑时，我躺在床上，

    他便伶伶俐俐地从我身上跨过，从我脚边飞去了。

    等我睁开眼和太阳再见，

    这算又溜走了一日。

    我掩着面叹息。

    但是新来的日子的影儿又开始在叹息里闪过了。

    在逃去如飞的日子里，在千门万户的世界里的我能做些什么呢？

    只有徘徊罢了，只有匆匆罢了；

    在八千多日的匆匆里，除徘徊外，又剩些什么呢？

    过去的日子如轻烟，被微风吹散了，如薄雾，被初阳蒸融了；

    我留着些什么痕迹呢？

    我何曾留着像游丝样的痕迹呢？

    我赤裸裸来到这世界，转眼间也将赤裸裸的回去罢？

    但不能平的，

    为什么偏要白白走这一遭啊？

    你聪明的，告诉我，

    我们的日子为什么一去不复返呢？

    """
    hide window
    return
