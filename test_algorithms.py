import unittest
from algorithms import bubblesort, find_highest_value, find_lowest_value, binary_search


unsorted = [3, 1, 2, 5, 4]


# Tests are running and passing but the project structure needs to be changed
class TestAlgorithms(unittest.TestCase):
    
    def test_bubblesort(self):
        bubblesort(unsorted)
        self.assertEqual(
            unsorted,
            [1, 2, 3, 4, 5]
        )

    def test_found_binary_search(self):
        self.assertEqual(
            # List index's start at 0 just like arrays in java
            binary_search(unsorted, 4),
            3
        )

    # Searching for an item that isn't present so -1 should be the correct response
    def test_unfound_binary_search(self):
        self.assertEqual(
            binary_search(unsorted, 6),
            -1
        )

    def test_find_highest_value(self):
        self.assertEqual(
            find_highest_value(unsorted),
            5
        )

    def test_find_lowest_value(self):
        self.assertEqual(
            find_lowest_value(unsorted),
            1
        )


if __name__ == '__main__':
    unittest.main()
