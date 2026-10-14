import unittest

from main import greet, calculate

class TestMain(unittest.TestCase):
    def test_greet_ohne_name(self):
        self.assertEqual(greet(),"Hello ")

    def test_greet_mit_name(self):
        self.assertEqual(greet("Max"),"Hello Max")

    def test_calculate_pos(self):
        self.assertEqual(calculate(2,144),146)

    def test_calculate_pos_neg(self):
        self.assertEqual(calculate(-555555,555555),0)


if __name__ == "__main__":
    unittest.main()

