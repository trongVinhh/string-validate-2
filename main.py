import re
import string
import random
import unittest


def validate_string(input_string):
    # Kiểm tra độ dài chuỗi
    if len(input_string) <= 8:
        return False

    # Kiểm tra không chứa khoảng trắng
    if " " in input_string:
        return False

    # Kiểm tra có đủ các loại ký tự
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for char in input_string:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True

    if not (has_lowercase and has_uppercase and has_digit and has_special):
        return False

    return True


class TestStringValidation(unittest.TestCase):
    def test_valid_string(self):
        valid_string = "Abcdefg123@"
        self.assertTrue(validate_string(valid_string))

    def test_short_string(self):
        short_string = "Abc1@"
        self.assertFalse(validate_string(short_string))

    def test_whitespace_string(self):
        whitespace_string = "Abc def1!"
        self.assertFalse(validate_string(whitespace_string))

    def test_missing_lowercase(self):
        missing_lowercase = "ABCDEFG123@"
        self.assertFalse(validate_string(missing_lowercase))

    def test_missing_uppercase(self):
        missing_uppercase = "abcdefg123@"
        self.assertFalse(validate_string(missing_uppercase))

    def test_missing_dig    it(self):
        missing_digit = "Abcdefg@"
        self.assertFalse(validate_string(missing_digit))

    def test_missing_special(self):
        missing_special = "Abcdefg123"
        self.assertFalse(validate_string(missing_special))


if __name__ == '__main__':
    unittest.main()