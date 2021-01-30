# 定义一个start.py ，启动文件展示最终存款金额
from select_money import show_money
from send_money import send_money

if __name__ == '__main__':
    send_money()
    show_money()

