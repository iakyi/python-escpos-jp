from src.escposjp import Dummy
from nose.tools import eq_


class testEscposJP:
    def setup(self):
        self.p = Dummy()

    def test_JpInit(self):
        self.p.hw("INIT")
        self.p.JpInit()
        eq_(self.p.output, b'\x1b@\x1bt\x01\x1cC\x01')

    def test_JpText(self):
        self.p.JpText("テスト")
        self.p.cut()
        eq_(self.p.output, b'\x1c&\x83e\x83X\x83g\x1c.\x1bd\x06\x1dV\x00')
