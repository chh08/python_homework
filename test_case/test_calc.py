# 定义计算器测试类
import pytest
import yaml
from calc_code.calc import calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    add_datas = datas['datas']
    myid = datas['myid']
    div_datas1 = datas['datas1']
    myid1 = datas['myid1']

class TestCalc:
    # 调用类前打印信息“start”
    def setup_class(self):
        print("start")
        self.calc = calculator()

    # 调用类后打印信息“end”
    def teardown_class(self):
        print("end")

    # 调用方法前打印信息“开始计算”
    def setup(self):
        print("开始计算")
        # 实例化计算器类
        self.calc = calculator()

    # 调用方法后打印信息“计算结束”
    def teardown(self):
        print("计算结束")
    # 参数化
    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=myid
    )
    # 定义加法
    def test_add(self, a, b, expect):
        # 调用add方法
        result = self.calc.add(a, b)
        # 判断result是浮点数，作出保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，断言
        assert result == expect


    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas1, ids=myid1
    )
    # 定义除法
    def test_div(self, a, b, expect):
        # 调用div方法
        result = self.calc.div(a, b)
        # 得到结果之后，断言
        assert result == expect