import pytest
from testcases.calcu import calcu

class Test_Cal():
    def test_add1(self):
        self.cal = calcu()
        res = calcu.add(self,10,20)
        assert res == 30
    def test_add2(self):
        self.cal = calcu()
        res = calcu.add(self,1,20)
        assert res == 30
    def test_mult1(self):
        self.cal = calcu()
        res = calcu.jian(self,30,20)
        assert res == 10
    def test_mult2(self):
        self.cal = calcu()
        res = calcu.jian(self,35,20)
        assert res == 10
    def test_div1(self):
        self.cal = calcu()
        res = calcu.div(self,30,20)
        assert res == 1.5
    def test_div2(self):
        self.cal = calcu()
        res = calcu.div(self,35,20)
        assert res == 10