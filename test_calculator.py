# https://github.com/HaowenYang2004/lab10-HY-ZH.git
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        # log(a, b): base=a, value=b
        # log(1, 5): base cannot be 1, should raise
        with self.assertRaises(ValueError):
            log(1, 5)
        # log(-2, 5): base cannot be negative, should raise
        with self.assertRaises(ValueError):
            log(-2, 5)
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