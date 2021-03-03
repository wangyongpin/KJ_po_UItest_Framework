import unittest

class testa(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None: # 类级别的
        cls.a = 1
        print('setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:# 类级别的
        print('tearDownClass')

    def setUp(self) -> None: # 方法级别的
        print('setUp')
        print('cls.a %s' % self.a)


    def tearDown(self) -> None:# 方法级别的
        print('tearDown')

    def test_01(self):
        print('test_01')
        self.assertTrue(True)

    def test_02(self):
        print('test_02')
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()