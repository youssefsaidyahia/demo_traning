import unittest

from wxample_copilet import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_true(self):
        self.assertTrue(is_palindrome('radar'))
        self.assertTrue(is_palindrome('Level'))
        self.assertTrue(is_palindrome('A'))

    def test_palindrome_false(self):
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('Python'))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))


if __name__ == '__main__':
    unittest.main()
