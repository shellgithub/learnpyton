import unittest
from lesson01.demo1 import sigmoid

from numpy import exp

class MyTestCase(unittest.TestCase):

    def test_sigmod(self):
        x = sigmoid(0)
        self.assertEqual(x, 0.5)

        x = sigmoid(10000)
        self.assertNotEqual(x, 1.0)

        x = sigmoid(-10000)
        self.assertNotEqual(x, 0.0)

if __name__ == '__main__':
    unittest.main()