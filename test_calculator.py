# https://github.com/HaowenYang2004/lab10-HY-ZH.git
# Partner 1: Haowen Yang
# Partner 2: Zixuan Huang
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-5, -4), -9)
        self.assertEqual(add(2, -7), -5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(2,3), -1)
        self.assertEqual(sub(-5,4), -9)
        self.assertEqual(sub(7,1), 6)


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(-1, 5),-5)
        self.assertEqual(mul(0, 100),0)

    def test_divide(self):
        self.assertEqual(div(2,10),5)
        self.assertAlmostEqual(div(3,7),2.333333, places=5)
        self.assertEqual(div(2,-8),-4)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # div(a, b) = b/a
        with self.assertRaises(ZeroDivisionError):
            div(0, 3)       # a = 0 is invalid


    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 1), 0)
        self.assertEqual(log(3, 9), 2)
        self.assertEqual(log(16, 4), 0.5)


    def test_log_invalid_base(self): # 1 assertion
        # log(a, b) = base a, value b
        with self.assertRaises(ValueError):
            log(1, 5)       # base = 1 is invalid


    ######## Partner 1
    def test_log_invalid_argument(self):
        # log(a, b): base=a, value=b
        # log(2, -5): value cannot be negative, should raise
        with self.assertRaises(ValueError):
            log(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0, places=5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0, places=5)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0, places=5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.414213, places=5)
# Do not touch this
if __name__ == "__main__":
    unittest.main()