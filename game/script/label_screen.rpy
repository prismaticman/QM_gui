screen label_screen(next_label):
    $ next_story = next_label
    tag menu
    add "images/beach01_evening by shazwan.jpg"
    add "images/label_mubu1.png" at mubu_transform1
    add "images/label_mubu.png" at mubu_transform2
    add "images/arc 00114.png" at logo_on
    use calendar(date_inf)
    timer 1.5 action Call(next_story)
#####################################################
# 初始化python
#
init python:

    # 引入datetime库中的date模块。
    # datetime库里有很多其他东西，不过这里我们用不到所以只引用date模块就行了。
    # date模块包含计算日期，在日期和字符间转换等功能。
    from datetime import date

    # 引入locale模块。locale模块可以获取本地的设置。比如这个电脑所在
    # 的国家和它的语言设置。
    # 当然还有我们需要的本地日期格式。
    import locale

    # 获取今天的日期并赋值给today。
    today = date.today()

    # 将所有的locale设置成用户默认的设置。
    locale.setlocale(locale.LC_ALL, '')

    # 设定本地日期格式并赋值给date_inf （这里使用一个包含键值对的字典类型）
    # 我们想在日历上显示的字符串。
    # 像日、年的值，和月份、星期的名称。（译注：英语环境下月份和星期都用字母表示）
    # 更多选项，请参见 strftime.org，或者搜索"python strftime"如果这个网站消失的话。
    date_inf = {    "day": today.strftime("%A"),
                    "daynr": today.strftime("%d"),
                    "month": today.strftime("%B"),
                    "year": today.strftime("%Y")
                }





#######################################################
# 定义日历的长相，使用的是 Ren'py的 screen 语句。
# 这个部分通常放在screens.rpy里，不过如果你是我，
# 可能马上就想贴到自己脚本里然后测试结果。
screen calendar(date_inf):

    # 不能阻止用户和其他东西交互，这个screen只用来显示信息。
    modal False

    # screen的其他部分。
    frame:
        xalign 1.0   # 放在右上角
        yalign 0.0    #
        xsize 100    # 大小是100*100像素
        ysize 100    #
        xmargin .05  # 和其他元素间留点儿距离
        ymargin .05   #
        xpadding .15 # 和内部内容留点儿距离
        ypadding .15 #

        vbox: # 放一个竖向排版的盒子。
            text date_inf["daynr"] size 60 xalign 0.5   # 在盒子正中大字显示日期。
            hbox: #放一个横向排版的盒子。
                text date_inf["month"] size 12 xalign 0.5 # 在盒子中间小字显示月和年。
                text date_inf["year"] size 12 xalign 0.5  #
                spacing 10 # 给两个条目之间留点距离。
