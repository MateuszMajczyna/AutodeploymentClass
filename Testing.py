import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Test data
        a = 5
        b = 10
        expected_sum = 15

        # Perform the test
        result = a + b

        # Assert that the result is equal to the expected sum
        self.assertEqual(result, expected_sum, "The addition result should equal the expected sum")


if __name__ == '__main__':
    unittest.main()