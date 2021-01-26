"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
"""
class Animal:
    """创建一个动物类"""

    def __init__(self,name, color, age, gender):
        """初始化属性"""
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
        self.calls = None

    def animal_info(self):
        print(f"这是一只{self.gender} {self.name},它的颜色是{self.color}，非常好看，今年{self.age}岁了")

    def animal_calls(self, call):
        """定义叫方法"""
        self.calls = call
        print(f"它的叫声是'{self.calls}！'")

    def animal_run(self):
        """定义跑方法"""
        print(f"{self.name}是一种跑得很快的动物！")


if __name__ == '__main__':
    dog = Animal("dog", "yellow", "6", "male")
    dog.animal_info()
    dog.animal_calls("wangwangwang")
    dog.animal_run()