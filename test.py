import unittest
from calculator import Count

class TestAdd(unittest.TestCase):

    def setUp(self):
        print("test add start")

    def tearDown(self):
        print("test add end")

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

class TestSub(unittest.TestCase):

    def setUp(self):
        print("test sub start")

    def tearDown(self):
        print("test sub end")

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)


if __name__ == '__main__':
    #unittest.main()

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
