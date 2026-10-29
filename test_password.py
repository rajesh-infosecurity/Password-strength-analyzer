import unittest
from main import analyze_password


class TestPasswordAnalyzer(unittest.TestCase):

    def test_empty_password(self):
        result, _ = analyze_password("")
        self.assertEqual(result, "Invalid")

    def test_short_password(self):
        result, _ = analyze_password("abc")
        self.assertEqual(result, "Weak")

    def test_common_password(self):
        result, _ = analyze_password("password123")
        self.assertEqual(result, "Weak")

    def test_suggestions(self):
        _, suggestions = analyze_password("abc")
        self.assertTrue(len(suggestions) > 0)


if __name__ == "__main__":
    unittest.main()