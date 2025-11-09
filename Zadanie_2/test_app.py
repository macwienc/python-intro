import unittest
from app import (
    is_valid_email,
    calculate_rectangle_area,
    filter_even_numbers,
    convert_date_format,
    is_palindrome
)

class TestAppFunctions(unittest.TestCase):

    def setUp(self):
        self.valid_email = "test@example.com"
        self.invalid_email = "bad@address"
        self.numbers = [1, 2, 3, 4, 5, 6]

    def test_valid_email(self):
        self.assertTrue(is_valid_email(self.valid_email))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email(self.invalid_email))

    def test_non_string_email(self):
        self.assertFalse(is_valid_email(12345))

    def test_area_correct(self):
        self.assertEqual(calculate_rectangle_area(5, 3), 15)

    def test_area_with_negative(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-2, 4)

    def test_area_with_wrong_type(self):
        with self.assertRaises(TypeError):
            calculate_rectangle_area("a", 2)

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers(self.numbers), [2, 4, 6])

    def test_filter_with_non_int(self):
        with self.assertRaises(TypeError):
            filter_even_numbers([1, "two", 3])

    def test_filter_empty_list(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_convert_date_valid(self):
        self.assertEqual(
            convert_date_format("2024-05-10", "%Y-%m-%d", "%d/%m/%Y"),
            "10/05/2024"
        )

    def test_convert_date_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("2024-05-10", "%d-%m-%Y", "%Y/%m/%d")

    def test_convert_date_invalid_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("not-a-date", "%Y-%m-%d", "%d/%m/%Y")

    def test_palindrome_true(self):
        self.assertTrue(is_palindrome("Kajak"))

    def test_palindrome_with_spaces_and_caps(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome("Python"))

if __name__ == "__main__":
    unittest.main()
