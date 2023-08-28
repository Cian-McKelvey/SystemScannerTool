import unittest
from system_scanner.equations import val_average

value_list = [5,5,5,5,5]


# Working correctly, again, just need to change structure
class TestEquations(unittest.TestCase):

    def test_val_average(self):
        self.assertEqual(
            val_average(value_list),
            5
        )


if __name__ == '__main__':
    unittest.main()