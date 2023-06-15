import unittest
from equations import val_average

value_list = [5,5,5,5,5]


# Working correctly, again, just need to change structure
class TestAlgorithms(unittest.TestCase):

    def test_val_average(self):
        self.assertEqual(
            val_average(value_list),
            5
        )


if __name__ == '__main__':
    unittest.main()