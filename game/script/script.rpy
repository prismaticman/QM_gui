# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
##开场的图片宏定义

image title_sky = "images/title_sky.jpg"
image title_text = "images/title_name.png"
image logo = "images/title_name.png"
image beach_night = "images/beach01_evening by shazwan.jpg"
image g_b_s = "images/character/girl_bigsmile.png"
image g_p = "images/character/girl_polize.png"
image g_s = "images/character/girl_smile.png"
image m_b_s = "images/character/man_bigsmile.png"
image m_p = "images/character/man_polize.png"
image m_s = "images/character/man_smile.png"
image hiyori = Live2D("live2d/Hiyori", base=0.6,loop = True,fade = True)
image Haru = Live2D("live2d/Haru", base=0.6,loop = True,fade = True)
image Mark = Live2D("live2d/Mark", base=0.6,loop = True,fade = True)
image Natori = Live2D("live2d/Natori", base=0.6,loop = True,fade = True)
image Rice = Live2D("live2d/Rice", base=0.6,loop = True,fade = True)

define e = Character("女")
define l = Character("男")
##开场画面
define Ds = Dissolve(0.2)



label splashscreen:

    scene title_sky at begin_background
    show title_text at begin_title_text
    pause 1.0
    hide title_text with dissolve
    hide title_sky
    return




# 游戏在此开始。

label start:
    call screen label_screen("story1")
    call screen label_screen("story2")
    call screen label_screen("story3")

    # 此处为游戏结尾。

    return
