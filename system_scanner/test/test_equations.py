import unittest
from system_scanner.equations import val_average, is_over_max_usage

value_list = [5, 6, 7, 8, 9]


# Working correctly, again, just need to change structure
class TestEquations(unittest.TestCase):

    def test_val_average(self):
        self.assertEqual(
            val_average(value_list),
            7
        )

    def test_is_over_max_usage(self):
        self.assertEqual(
            is_over_max_usage(value_list, 8),
            True
        )


if __name__ == '__main__':
    unittest.main()