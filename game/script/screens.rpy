################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    # 解决断裂
    thumb_offset 2
    # 防止滑块超出bar
    top_gutter 2
    bottom_gutter 2
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内界面
################################################################################


## 对话界面 ########################################################################
##
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say



screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" at say_text_fade
                at say_namebox_trans

        ##text what id "what" at what_text_fade
        if renpy.is_seen(ever = True): # ever 为false时对本次运行起效，此处需要对过去所有阅读起效
            text what id "what" color "#BFD4CB" at what_text_fade# 标记颜色
        else:
            text what id "what" color "#FFFFFF" at what_text_fade# 未读颜色

    key "rollback" action ShowMenu('history') # 鼠标滚轮打开历史记录

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu
transform say_text_fade:
    xalign 1.0
    yoffset 50

transform what_text_fade:
    yalign 0.5
    xalign 0.5


transform say_namebox_trans:
    xalign 0.15 yalign -0.27
    alpha 0.0
    linear 0.15 alpha 1.0

transform say_windows_trans:

    yoffset 190
    linear 0.1 yoffset 0

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    yoffset 37
    # background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    background At("gui/textbox.png", say_windows_trans)

## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此界面必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    add "gui/frame_1.png":
        xalign 0.5 yalign 0.5
    style_prefix "input"
    hbox:
        xalign 0.5
        yalign 0.5
        text prompt style "input_prompt"
        input id "input" copypaste True


style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################
##
## 此界面用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        spacing 50
        for i in items:
            textbutton i.caption action i.action at screen_choice_animal


## 若为 True，菜单内的叙述会使用旁白角色。若为 False，叙述会显示为菜单内的文字说
## 明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    ## 确保该菜单出现在其他界面之上，
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("快存") action QuickSave()
            textbutton _("快读") action QuickLoad()
            textbutton _("设置") action ShowMenu('preferences')


## 此语句确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”界面。
##init python:
##    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("开始游戏") action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        textbutton _("读取游戏") action ShowMenu("load")

        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题界面") action MainMenu()

        textbutton _("关于") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必需或相关。
            textbutton _("帮助") action ShowMenu("help")

        if renpy.variant("pc"):

            ## “退出”按钮在 iOS 上被禁止设置，在安卓和网页上也不是必需的。
            textbutton _("退出") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu

##标题菜单界面定义区
image main_image = Movie(play="audio/main_background.webm", pos=(0, 0), anchor=(0, 0))
# 文字本体样式
style main_menu_button_text_fill:
    yoffset -6
    align (0.5, 0.5)
    size 45
    font "MaShanZheng-Regular.ttf"
    color "#81B8C4"
    outlines [(1.5, "#06667A", 0, 0)]
##标题的文字样式
style main_menu_text_style:
    size 120
    font "LongCang-Regular.ttf"
    color "#080C81"
    outlines [(4, "#24BEC7", 0, 0)]

style main_menu_text_style_zhu:
    size 120
    font "LongCang-Regular.ttf"
    color "#D02000"
    outlines [(4, "#8B2000", 0, 0)]

##标题的按钮
image new_game_button_text:
    Text("开始", style = "main_menu_button_text_fill")

image load_game_button_text:
    Text("继续", style = "main_menu_button_text_fill")

image preference_button_text:
    Text("设置", style = "main_menu_button_text_fill")

image about_button_text:
    Text("关于", style = "main_menu_button_text_fill")

image help_button_text:
    Text("帮助", style = "main_menu_button_text_fill")

image quit_button_text:
    Text("离开", style = "main_menu_button_text_fill")



##标题的文字

image main_menu_jian_text:
    Text("剪", style = "main_menu_text_style")
image main_menu_zhu_text:
    Text("烛", style = "main_menu_text_style_zhu")
image main_menu_xi_text:
    Text("西", style = "main_menu_text_style")
image main_menu_chuang_text:
    Text("窗", style = "main_menu_text_style")

screen main_menu():

    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu


    add "main_image" at main_menu_background_animation
    add "main_menu_jian_text" at main_menu_jian_animation
    add "main_menu_zhu_text" at main_menu_zhu_animation
    add "main_menu_xi_text" at main_menu_xi_animation
    add "main_menu_chuang_text" at main_menu_chuang_animation

    vbox:
        xalign 0.96
        yalign 0.5
        spacing 50
        imagebutton:
            idle "gui/button/main_menu_button.png"
            foreground "new_game_button_text"
            hover_sound "audio/se_saa06.wav"
            at main_menu_button_left
            action Start()
        imagebutton:
            idle "gui/button/main_menu_button.png"
            foreground "load_game_button_text"
            hover_sound "audio/se_saa06.wav"
            at main_menu_button_right
            action ShowMenu("load")
        imagebutton:
            idle "gui/button/main_menu_button.png"
            foreground "preference_button_text"
            hover_sound "audio/se_saa06.wav"
            at main_menu_button_left
            action ShowMenu("main_preferences")
        imagebutton:
            idle "gui/button/main_menu_button.png"
            foreground "quit_button_text"
            hover_sound "audio/se_saa06.wav"
            at main_menu_button_right
            action Quit(confirm=not main_menu)

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

#    use navigation

    textbutton _("返回"):
        style "return_button"
        hover_sound "audio/se_saa04.wav"
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”界面到此处。子级“vbox”将包含在“game_menu”界面
    ## 的“viewport”内。
##    use game_menu(_("关于"), scroll="viewport"):

##        style_prefix "about"

    vbox:

        label "[config.name!t]"
        text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
        if gui.about:
            text "[gui.about!t]\n"

        text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]\n\n[renpy.license!t]")

        textbutton _("返回"):
            yalign 0.5
            action Return()
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存界面 #####################################################################
##
## 这些界面负责让玩家保存游戏并能够再次读取。由于它们几乎完全一样，因此它们都是
## 以第三方界面“file_slots”来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load

style solt_time_button_text:
    xalign 1.0
    yalign 0.5
    font "MaShanZheng-Regular.ttf"
    size 25
    color "#DEF3EA"

style solt_page_button_text:
    xalign 0.5
    yalign 0.21
    font "MaShanZheng-Regular.ttf"
    size 30
    color "#FFFFFF"

style solt_title_text:
    xalign 0.5
    yalign 0.14
    font "MaShanZheng-Regular.ttf"
    size 50
    color "#FFFFFF"

screen save():

    $ pagevalue = FilePageName(auto="自动存档", quick="快速存档")
    tag menu
    text "保存":
        style "solt_title_text"
    text "[pagevalue]":
        style "solt_page_button_text"
    use file_slots(_("保存"))


screen load():
    $ pagevalue = FilePageName(auto="自动存档", quick="快速存档")
    tag menu
    text "读取":
        style "solt_title_text"
    text "[pagevalue]":
        style "solt_page_button_text"
    use file_slots(_("读取游戏"))

screen main_load():
    $ pagevalue = FilePageName(auto="自动存档", quick="快速存档")
    tag menu
    text "读取":
        style "solt_title_text"
    text "[pagevalue]":
        style "solt_page_button_text"
    use file_slots_main(_("读取游戏"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    ##use game_menu(title):
    add "gui/background2.png" at setting_bg_transform
    fixed:

            ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。

            ## 页面名称，可以通过单击按钮进行编辑。


            ## 存档位网格。
        grid 2 2:#gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.42
            spacing 50##gui.slot_spacing
            at save_screen_file
            for i in range(4): #(gui.file_slot_cols * gui.file_slot_rows):


                $ slot = i + 1

                button:
                    background Frame(im.AlphaMask("gui/nodata1.png","gui/testmask.png"))
                    action FileAction(slot)
                    has hbox
                    spacing 12
                    add im.AlphaMask(FileScreenshot(slot,empty="gui/nodata.png"), "gui/testmask.png") xalign 0.5


                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                        style "solt_time_button_text"

                    text FileSaveName(slot):
                        style "solt_time_button_text"
                    at save_screen_file
                    key "save_delete" action FileDelete(slot)
            ## 用于访问其他页面的按钮。
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 0.73

            spacing 20##gui.page_spacing


            if config.has_autosave:
                imagebutton:
                    foreground Text("{#auto_page}A",xalign = 0.5,yalign = 0.3,size = 100)
                    idle "gui/button/save_selet_button_idle.png"
                    selected_hover "gui/button/save_selet_button.png"
                    selected_idle "gui/button/save_selet_button.png"
                    at save_screen_auto
                    action FilePage("auto")
                ##textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                imagebutton:
                    foreground Text("{#quick_page}Q",xalign = 0.5,yalign = 0.3,size = 100)
                    idle "gui/button/save_selet_button_idle.png"
                    selected_hover "gui/button/save_selet_button.png"
                    selected_idle "gui/button/save_selet_button.png"
                    at save_screen_auto
                    action FilePage("quick")
                ##textbutton _("{#quick_page}Q") action FilePage("quick")

                ## “range(1, 10)”给出 1 到 9 之间的数字。

            for page in range(1, 10):
                imagebutton:
                    foreground Text(text=str(page),xalign = 0.5,yalign = 0.3,size = 100)
                    idle "gui/button/save_selet_button_idle.png"
                    selected_hover "gui/button/save_selet_button.png"
                    selected_idle "gui/button/save_selet_button.png"
                    at save_screen_auto
                    action FilePage(page)
                ##textbutton "[page]" action FilePage(page)

    imagebutton:
        idle "images/gallery_next2.png"
        hover "images/gallery_next.png"
        hover_sound "audio/se_saa04.wav"
        at save_screen_next
        action FilePageNext()
    imagebutton:
        idle "images/gallery_prev2.png"
        hover "images/gallery_prev.png"
        hover_sound "audio/se_saa04.wav"
        at save_screen_prev
        action FilePagePrevious()

    hbox:
        xalign 0.5
        yalign 0.85
        spacing 50
        imagebutton:
            idle "images/base_003.png"
            hover "images/base_003_hover.png"
            foreground Text("返回",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Return()
        imagebutton:
            idle "images/base_003.png"
            hover "images/base_003_hover.png"
            foreground Text("标题",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action MainMenu()
        imagebutton:
            idle "images/base_003.png"
            hover "images/base_003_hover.png"
            foreground Text("退出",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Quit(confirm=not main_menu)

screen file_slots_main(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))
    ##use game_menu(title):
    add "gui/background2.png" at setting_bg_transform
    fixed:

            ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。

            ## 页面名称，可以通过单击按钮进行编辑。


            ## 存档位网格。
        grid 2 2:#gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"

            xalign 0.5
            yalign 0.42
            spacing 50##gui.slot_spacing
            at save_screen_file
            for i in range(4): #(gui.file_slot_cols * gui.file_slot_rows):


                $ slot = i + 1

                button:
                    background Frame(im.AlphaMask("gui/nodata1.png","gui/testmask.png"))
                    action FileAction(slot)
                    has hbox
                    spacing 12
                    add im.AlphaMask(FileScreenshot(slot,empty="gui/nodata.png"), "gui/testmask.png") xalign 0.5


                    text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                        style "solt_time_button_text"

                    text FileSaveName(slot):
                        style "solt_time_button_text"
                    at save_screen_file
                    key "save_delete" action FileDelete(slot)
            ## 用于访问其他页面的按钮。
        hbox:
            style_prefix "page"

            xalign 0.5
            yalign 0.73

            spacing 20##gui.page_spacing


            if config.has_autosave:
                imagebutton:
                    foreground Text("{#auto_page}A",xalign = 0.5,yalign = 0.3,size = 100)
                    idle "gui/button/save_selet_button_idle.png"
                    selected_hover "gui/button/save_selet_button.png"
                    selected_idle "gui/button/save_selet_button.png"
                    at save_screen_auto
                    action FilePage("auto")
                ##textbutton _("{#auto_page}A") action FilePage("auto")

            if config.has_quicksave:
                imagebutton:
                    foreground Text("{#quick_page}Q",xalign = 0.5,yalign = 0.3,size = 100)
                    idle "gui/button/save_selet_button_idle.png"
                    selected_hover "gui/button/save_selet_button.png"
                    selected_idle "gui/button/save_selet_button.png"
                    at save_screen_auto
                    action FilePage("quick")
                ##textbutton _("{#quick_page}Q") action FilePage("quick")

                ## “range(1, 10)”给出 1 到 9 之间的数字。

            for page in range(1, 10):
                imagebutton:
                    foreground Text(text=str(page),xalign = 0.5,yalign = 0.3,size = 100)
                    idle "gui/button/save_selet_button_idle.png"
                    selected_hover "gui/button/save_selet_button.png"
                    selected_idle "gui/button/save_selet_button.png"
                    at save_screen_auto
                    action FilePage(page)
                ##textbutton "[page]" action FilePage(page)

    imagebutton:
        idle "images/gallery_next2.png"
        hover "images/gallery_next.png"
        hover_sound "audio/se_saa04.wav"
        at save_screen_next
        action FilePageNext()
    imagebutton:
        idle "images/gallery_prev2.png"
        hover "images/gallery_prev.png"
        hover_sound "audio/se_saa04.wav"
        at save_screen_prev
        action FilePagePrevious()

    hbox:
        xalign 0.5
        yalign 0.85
        spacing 50
        imagebutton:
            idle "images/base_003.png"
            hover "images/base_003_hover.png"
            foreground Text("返回",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Return()

        imagebutton:
            idle "images/base_003.png"
            hover "images/base_003_hover.png"
            foreground Text("退出",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Quit(confirm=not main_menu)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置界面 ########################################################################
##
## 设置界面允许玩家配置游戏以更好地适应自己的习惯。
##
## https://www.renpy.cn/doc/screen_special.html#preferences
style sc_title_style:
    font "MaShanZheng-Regular.ttf"
    size 49
    ypos 32
    color "#868686"

style system_text_style:
    align (0.5, 0.5)
    font "MaShanZheng-Regular.ttf"
    size 24
    color "#FFFFFF"

screen setting_bg(sc_title):

    add "gui/background3.png" at setting_bg_transform

    ## 中文标题覆盖在英文标题上面
    text sc_title:
        style "sc_title_style"
        at setting_text_transform



screen preferences():

    tag menu

    modal True

    zorder 50

    use setting_bg("设置")

    # 测试用返回按钮
    frame:
        background None
        xpadding 280
        ypadding 10
        xalign 0.5
        yalign 0.48
        vbox:
            spacing 10
            text "文字速度":
                at setting_screen_bar(0.15)

            bar value Preference("text speed") at setting_screen_bar(0.15)

            text "音乐音量":
                 at setting_screen_bar(0.25)

            bar value Preference("music volume") at setting_screen_bar(0.25)

            text "音效音量":
                 at setting_screen_bar(0.35)

            bar value Preference("sound volume") at setting_screen_bar(0.35)
    hbox:
        xalign 0.5
        yalign 0.85
        spacing 50
        imagebutton:
            idle "images/base_004.png"
            hover "images/base_004_hover.png"
            foreground Text("返回",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Return()
        imagebutton:
            idle "images/base_004.png"
            hover "images/base_004_hover.png"
            foreground Text("标题",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action MainMenu()
        imagebutton:
            idle "images/base_004.png"
            hover "images/base_004_hover.png"
            foreground Text("退出",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Quit(confirm=not main_menu)


screen main_preferences():

    tag menu

    modal True

    zorder 50

    use setting_bg("设置")

    # 测试用返回按钮
    frame:
        background None
        xpadding 280
        ypadding 10
        xalign 0.5
        yalign 0.48
        vbox:
            spacing 10
            text "文字速度":
                at setting_screen_bar(0.15)

            bar value Preference("text speed") at setting_screen_bar(0.15)

            text "音乐音量":
                 at setting_screen_bar(0.25)

            bar value Preference("music volume") at setting_screen_bar(0.25)

            text "音效音量":
                 at setting_screen_bar(0.35)

            bar value Preference("sound volume") at setting_screen_bar(0.35)
    hbox:
        xalign 0.5
        yalign 0.85
        spacing 50
        imagebutton:
            idle "images/base_004.png"
            hover "images/base_004_hover.png"
            foreground Text("返回",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Return()

        imagebutton:
            idle "images/base_004.png"
            hover "images/base_004_hover.png"
            foreground Text("退出",xalign = 0.5,yalign = 0.3,size = 25)
            hover_sound "audio/se_saa04.wav"
            at setting_screen_button
            action Quit(confirm=not main_menu)


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## 历史界面 ########################################################################
##
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html

##历史界面样式

# log界面主体显示区域样式
style log_frame_style:
    left_padding 265
    right_padding 265

# log界面文本标签区域样式
style log_label_frame_style:
    top_padding 20
    xfill True

# log界面窗口区域样式
style log_history_window_frame_style:
    top_padding 135
    bottom_padding 90
    xfill True

# log文本样式
style log_text_style:
    color "#cccccc"
    # 根据自己需要修改文本字体，这里用的是汉仪细简黑简
    font "NotoSansSC-Light.otf"
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

screen history():




    tag menu

    # 不使用预加载
    predict False

    add "gui/log_base.png" at history_background

    frame:
        style "log_frame_style"


        frame:
            style "log_history_window_frame_style"


            vpgrid:
                cols 1
                yinitial 1.0

                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True

                # 确保整个Frame塞满
                side_yfill True
                side_xfill True

                for h in _history_list:

                    window:
                        background None

                        ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条目。
                        has fixed:
                            yfit True

                        if h.who:

                            label h.who:
                                style "history_name"
                                substitute False
                                ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述人文本中。
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]

                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            # 直接使用history_text，也可以自定义其他样式
                            style "log_text_style"
                            substitute False
                if not _history_list:
                    label _("尚无对话历史记录。")

    imagebutton:
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("返回",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at history_return_button
        action Return()

## 此语句决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    ##use game_menu(_("帮助"), scroll="viewport"):

    style_prefix "help"

    vbox:
        spacing 15

        use mouse_help()
    textbutton _("返回"):
        xalign 0.5
        action Return()
screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话但不激活选项。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上\n点击回退操作区")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此界面时，确保其他界面无法输入。
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    add "gui/frame.png" at YN_back_ground


    label _(message):

        style "confirm_prompt"
        xalign 0.5 yalign 0.5

    imagebutton:
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("是",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa06.wav"
        at yes_button_animation
        action yes_action

    imagebutton:
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("否",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at no_button_animation
        action no_action
    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示界面 ######################################################################
##
## “skip_indicator”界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text "快" at skip_animal(0) style "solt_page_button_text"
            text "进" at skip_animal(0.11) style "solt_page_button_text"
            text "中" at skip_animal(0.22) style "solt_page_button_text"
            text "." at skip_animal(0.33) style "skip_triangle"
            text "." at skip_animal(0.44) style "skip_triangle"
            text "." at skip_animal(0.55) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式界面 ####################################################################
##
## 此界面用于 NVL 模式的对话和菜单。
##
## https://www.renpy.cn/doc/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此语句控制一次可以显示的 NVL 模式条目的最大数量。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

screen quick_menu():
    zorder 100
    imagebutton:
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("菜单",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at index_menu_button
        action ShowMenu('index_menu')






## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen index_menu():


    tag menu
    imagebutton:
        xalign 0.75 yalign 0.40
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("读取",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at quick_menu_button(3)
        action ShowMenu('load')
    imagebutton:
        xalign 0.75 yalign 0.50
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("保存",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at quick_menu_button(2)
        action ShowMenu('save')
    imagebutton:
        xalign 0.75 yalign 0.60
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("设置",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at quick_menu_button(1)
        action ShowMenu('preferences')
    imagebutton:
        xalign 0.75 yalign 0.70
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("历史",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at quick_menu_button(1)
        action ShowMenu('history')
    imagebutton:
        xalign 0.75 yalign 0.80
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("快进",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at quick_menu_button(2)
        action Skip() alternate Skip(fast=True, confirm=True)
    imagebutton:
        xalign 0.75 yalign 0.90
        idle "images/base_004.png"
        hover "images/base_004_hover.png"
        foreground Text("返回",xalign = 0.5,yalign = 0.38,size = 25)
        hover_sound "audio/se_saa04.wav"
        at quick_menu_button(3)
        action Return()
##    textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
##    textbutton _("自动") action Preference("auto-forward", "toggle")
##     textbutton _("历史") action ShowMenu('history')
##     textbutton _("保存") action ShowMenu('save')
##     textbutton _("设置") action ShowMenu('preferences')
##

style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
