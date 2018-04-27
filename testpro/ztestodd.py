import unittest
from common import CommonHead
from calculator import Count


class TestOdd(CommonHead):

    def test_odd(self):
        j = Count(1, 3)
        self.assertEqual(j.add(), 4)


if __name__ == '__main__':
    unittest.main()