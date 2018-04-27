import unittest
#from testadd import TestAdd
#from testsub import TestSub


# 构造测试集
#suite = unittest.TestSuite()
#suite.addTest(TestAdd("test_add"))
#suite.addTest(TestAdd("test_add2"))
#suite.addTest(TestSub("test_sub"))
#suite.addTest(TestSub("test_sub2"))

test_dir = "./testpro/"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="ztest*.py")

if __name__ == '__main__':
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(discover)
    #runner.run(suite)