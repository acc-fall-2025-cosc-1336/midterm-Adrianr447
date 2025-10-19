import os
import sys
# Add repo root to sys.path so imports like `from src...` work during discovery
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import unittest
from src.question_c.days import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_q3_days_invalid_low(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")

    def test_q3_days_valids(self):
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")

    def test_q3_days_invalid_high(self):
        self.assertEqual(get_day_of_week(8), "Invalid number")

if __name__ == "__main__":
    unittest.main()

# Added for running tests with discovery
# Command: python3 -m unittest discover -s tests -p "question_tests.py" -v


