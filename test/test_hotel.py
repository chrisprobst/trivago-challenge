import unittest

from hotel import Hotel
from util import is_printable


class TestHotel(unittest.TestCase):
    def test_validate(self):
        h = Hotel(name='Hotel 1',
                  address='Street 1337',
                  stars=4,
                  contact='Mr. Hotel',
                  phone='0000-0000',
                  uri='https://google.com')

        self.assertIsNone(h.validate())

        h2 = Hotel(name='\u0001',
                   address='Street 1337',
                   stars=4,
                   contact='Mr. Hotel',
                   phone='0000-0000',
                   uri='https://google.com')

        self.assertEqual(h2.validate(), 'Name not printable (\u0001)')

        h3 = Hotel(name='Hotel 1',
                   address='Street 1337',
                   stars=-4,
                   contact='Mr. Hotel',
                   phone='0000-0000',
                   uri='https://google.com')

        self.assertEqual(h3.validate(), 'Stars not between 0 and 5')

        h4 = Hotel(name='Hotel 1',
                   address='Street 1337',
                   stars=4,
                   contact='Mr. Hotel',
                   phone='0000-0000',
                   uri='google.com')

        self.assertEqual(h4.validate(), 'URI "google.com" is malformed')
