import time


def get_title():
    # 获得当前的时间，例如01月24日
    current_time = time.localtime()
    current_date = time.strftime("%m月%d日", current_time)

    art_title = current_date + "资讯(新闻、科技、金融、AI)"
    return art_title