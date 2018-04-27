import unittest
from calculator import Count

class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

if __name__ == '__main__':
    #unittest.main()

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
