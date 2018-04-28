import sys
import unittest

sys.path.append("../UnittestContain/")

class CommonHead(unittest.TestCase):

    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")
