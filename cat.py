"""
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""
from animal import Animal


class Cat(Animal):
    """创建cat类"""
    def __init__(self, name, color, age, gender, hair):
        self.hair = hair
        """继承父类方法"""
        super(Cat, self).__init__(name, color, age, gender)

    def animal_info(self):
        """info输出增加hair属性"""
        print(f"这是一只{self.gender} {self.name},它的颜色是{self.color}，非常好看的{self.hair}，今年{self.age}岁了")

    def animal_calls(self, call=None):
        """重写叫方法"""
        super(Cat, self).animal_calls('miaomiaomiao')

    def hunting(self):
        """定义一个捕猎方法"""
        print(f"{self.name}是一个捕鼠高手，死在它手下的鼠不计其数")

        
if __name__ == '__main__':
    cat = Cat('cat', 'red', '2', 'female', 'short hair')
    cat.animal_info()
    cat.animal_calls()
    """直接调用父类run方法"""
    cat.animal_run()
    cat.hunting()
