import main as main

import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(main.sum(1, 2), 3, "Should be 3")

    def test_mul(self):
        self.assertEqual(main.mul(1, 2), 2, "Should be 2")
        
    def test_sub(self):
        self.assertEqual(main.sub(1, 2), -1, "Should be -1")
        
    def test_div(self):
        self.assertEqual(main.div(4, 2), 2, "Should be 2")

    #def test_div_false(self):
    #    self.assertEqual(main.div(4, 2), 3, "False Test Check")

if __name__ == '__main__':
    unittest.main()
