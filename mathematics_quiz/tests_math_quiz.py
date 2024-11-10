import unittest
from math_quiz import RandomInteger, RandomOperation, CalculateOperation

class TestMathGame(unittest.TestCase):

    def test_RandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = RandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_RandomOperation(self):
        # Test if RandomOperation returns one of the expected operations.
        for _ in range(1000): 
            result = RandomOperation()
            self.assertIn(result, ['+', '-', '*'])

    def test_CalculateOperation(self):
        
        # Test if CalculateOperation returns one of the expected answer.
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '+', '8 + 3', 11),
            (10, 4, '-', '10 - 4', 6),
            (6, 3, '*', '6 * 3', 18),
            (15, 2, '+', '15 + 2', 17),
            (7, 2, '-', '7 - 2', 5),
            (9, 3, '*', '9 * 3', 27),
            (12, 6, '+', '12 + 6', 18),
            (14, 7, '-', '14 - 7', 7),
            ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            process_string, result = CalculateOperation(num1, num2, operator)
            self.assertEqual(expected_answer, result)
            
if __name__ == "__main__":
    unittest.main()
