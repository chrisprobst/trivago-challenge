import unittest

from hotel import Hotel
from parsing import parse_hotels, write_hotels
from util import is_printable


class TestParsing(unittest.TestCase):
    def test_parse_hotels(self):
        parsed_hotels = parse_hotels('test/test.csv')
        final_hotels = [Hotel(name='Hotel 1',
                              address='Street 1337',
                              stars=4,
                              contact='Mr. Hotel',
                              phone='0000-0000',
                              uri='https://google.com')]

        self.assertEqual(parsed_hotels, final_hotels)

    def test_write_hotels(self):
        final_hotels = [Hotel(name='Hotel 1',
                              address='Street 1337',
                              stars=4,
                              contact='Mr. Hotel',
                              phone='0000-0000',
                              uri='https://google.com')]

        write_hotels(final_hotels, 'test/test_output.csv')
        parsed_hotels = parse_hotels('test/test_output.csv')

        self.assertEqual(parsed_hotels, final_hotels)
