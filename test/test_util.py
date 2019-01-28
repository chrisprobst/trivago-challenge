import unittest

from util import is_printable


class TestUtil(unittest.TestCase):
    def test_is_printable(self):
        self.assertTrue(is_printable('hello'))
        self.assertTrue(is_printable(' ' * 10))
        self.assertTrue(is_printable(''))
        self.assertFalse(is_printable('\u0001'))

