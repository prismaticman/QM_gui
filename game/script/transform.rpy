##开场界面
##开场背景
transform begin_background:
    xalign 0.0 yalign 1.0
    linear 1.0 yalign 0.0

##开场文字

transform begin_title_text:
    xalign 0.5 yalign 0.5 alpha 0.0
    on show:
        time 0.5
        linear 0.5 alpha 1.0


##主菜单界面
##主菜单的按钮转场

transform main_menu_button_right:
    xoffset -10.0 alpha 0.0 zoom 1.3
    on start:
        time 0.4
        linear 0.4 xoffset 0.0 alpha 1.0


transform main_menu_button_left:
    xoffset 10.0 alpha 0.0 zoom 1.3
    on start:
        time 0.4
        linear 0.4 xoffset 0.0 alpha 1.0

##主菜单的标题文字
transform main_menu_jian_animation:
    xalign 0.10 yalign 0.15 yzoom 1.45 alpha 0.0 yoffset -40.0
    linear 0.8 alpha 1.0 yoffset 0.0


transform main_menu_zhu_animation:
    xalign 0.10 yalign 0.40 yzoom 1.45 alpha 0.0 yoffset -40.0
    linear 0.8 alpha 1.0 yoffset 0.0
    on start:
        linear 1.8 matrixcolor BrightnessMatrix(0.0)
        linear 1.8 matrixcolor BrightnessMatrix(0.25)
        repeat


transform main_menu_xi_animation:
    xalign 0.21 yalign 0.38 yzoom 1.30 alpha 0.0
    on start:
        time 0.8
        linear 0.4 alpha 1.0

transform main_menu_chuang_animation:
    xalign 0.21 yalign 0.63 yzoom 1.30 alpha 0.0
    on start:
        time 0.8
        linear 0.4 alpha 1.0



##主菜单的背景转场
transform main_menu_background_animation:
    matrixcolor BrightnessMatrix(-0.25) alpha 0.5
    linear 1.0 alpha 1.0

##确认界面
##确认界面的背景
transform YN_back_ground:
    xalign 0.5 yalign 0.5 alpha 0.0
    linear 0.4 alpha 1.0
##是否的按钮
transform yes_button_animation:
    xalign 0.38 yalign 0.65 alpha 0.0 xoffset -20.0 yoffset -10 zoom 1.5
    on start:
        linear 0.15 alpha 1.0 xoffset 0.0
    on hide:
        linear 0.15 alpha 0.0 xoffset -20

transform no_button_animation:
    xalign 0.62 yalign 0.65 alpha 0.0 xoffset 20 yoffset -10 zoom 1.5
    on start:
        linear 0.15 alpha 1.0 xoffset 0.0
    on hide:
        linear 0.15 alpha 0.0 xoffset 20
##快捷菜单的按钮
transform quick_menu_button(delay):
    xoffset 20 alpha 0.0 zoom 1.5
    on start:
        time delay*0.07
        linear 0.18 xoffset 0.0 alpha 1.0

##引导界面menu按钮
transform index_menu_button:
    xalign 0.89 yalign 0.72 zoom 1.5
##历史界面
##历史界面背景动画
transform history_background:
    alpha 0.0 xalign 0.5 yalign 0.5
    on start:
        linear 0.5 alpha 0.5
##历史界面文字动画

##历史界面按钮
transform history_return_button:
    xalign 0.18 yalign 0.9 zoom 1.5 alpha 0.0 xoffset -20
    on start:
        linear 0.45 alpha 1.0 xoffset 0.0
##设置界面背景
transform setting_bg_transform:
    xalign 0.5 yalign 0.5 yoffset -30 alpha 0.0
    linear 0.5 yoffset 0.0 alpha 1.0
##设置界面文字
transform setting_text_transform:
    xalign 0.5 yalign 0.18 alpha 0.0 yoffset -10
    pause 0.35
    linear 0.15 yoffset 0.0 alpha 1.0
#设置界面滑条
transform setting_screen_bar(delay):
    xoffset -33 alpha 0.0
    pause 0.33
    linear delay xoffset 0.0 alpha 1.0
#设置界面按钮
transform setting_screen_button:
    zoom 1.5 yoffset -25 alpha 0.0
    linear 0.3 yoffset 0.0 alpha 1.0
#存档界面背景
transform save_screen_bg:
    xalign 0.5 yalign 0.5
#存档界面前进后退按钮
transform save_screen_next:
    xalign 0.84 yalign 0.4
    xoffset 15 alpha 0.0
    pause 0.2
    linear 0.35 xoffset 0 alpha 1.0
transform save_screen_prev:
    xalign 0.16 yalign 0.4
    xoffset -15 alpha 0.0
    pause 0.2
    linear 0.4 xoffset 0 alpha 1.0
#存档界面自动存档按钮
transform save_screen_auto:
    zoom 0.3
    on start:
        yoffset -20 alpha 0.0
        linear 0.25 yoffset 0.0 alpha 1.0
##存档按钮
transform save_screen_file:
    yoffset -20 alpha 0.0
    on start:
        linear 0.5 yoffset 0 alpha 1.0
##幕布的转场
transform mubu_transform1:
    xalign 0.5 yalign 1.25
    linear 0.25 yalign 1.15
    pause 1.0
    linear 0.25 alpha 0.0


transform mubu_transform2:
    xalign 0.5 yalign -0.25
    linear 0.25 yalign -0.15
    pause 1.0
    linear 0.25 alpha 0.0

transform logo_on:
    xalign 0.65 yalign 1.0 zoom 2.1 alpha 0.0
    linear 0.4 xalign 0.75 alpha 1.0
    pause 0.7
    linear 0.4 xalign 0.65 alpha 0.0
#快进键动画
transform skip_animal(delay_s):
    xalign 0.5 yalign 0.5
    pause delay_s
    block:
        linear 0.25 yoffset -5
        linear 0.25 yoffset 5
        repeat
##选择界面
transform screen_choice_animal:
    xoffset -20 alpha 0.0
    linear 0.25 xoffset 0.0 alpha 1.0
