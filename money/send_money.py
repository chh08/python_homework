# 定义发工资模块 send_money，用来增加收入计算
import money


def send_money():
    """定义发工资模块"""
    salary = 1000
    print("今天是发工资的时间")
    money.save_money = money.save_money + salary
    print(f"这个月工资收入为{salary}元")

# send_money()
