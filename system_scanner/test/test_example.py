import unittest


# Test file to make sure tests run correctly, can change 2 to another value to check if the tests fail correctly
class TestExample(unittest.TestCase):

    def test_addition(self):
        addition = 1 + 1
        self.assertEqual(addition, 2)


if __name__ == '__main__':
    unittest.main()