from dataclasses import dataclass, asdict

import validators

from util import is_printable


@dataclass
class Hotel:
    name: str
    address: str
    stars: int
    contact: str
    phone: str
    uri: str

    def validate(self):
        """
        Validates the hotel attributes based on the following rules:
        - "name" must be printable (whitespaces are ok)
        - "address" must be printable (whitespaces are ok)
        - "stars" must be between 0 and 5 (incl.)
        - "contact" must be printable (whitespaces are ok)
        - "uri" must be a valid url (based on validators package, related to https://gist.github.com/dperini/729294)

        :return:
        None if the hotel is valid, otherwise a string which contains the reason for the failed validation.
        """

        if not is_printable(self.name):
            return 'Name not printable ({})'.format(self.name)

        if not is_printable(self.address):
            return 'Address not printable ({})'.format(self.address)

        try:
            self.stars = int(self.stars)
            if not (0 <= self.stars <= 5):
                return 'Stars not between 0 and 5'
        except ValueError:
            return 'Stars "{}" cannot be parsed as int'.format(self.stars)

        if not is_printable(self.contact):
            return 'Contact not printable ({})'.format(self.contact)

        if not is_printable(self.phone):
            return 'Phone not printable ({})'.format(self.phone)

        if not validators.url(self.uri):
            return 'URI "{}" is malformed'.format(self.uri)

    def asdict(self):
        """
        :return:
        The hotel as dict with field names as keys.
        """
        return asdict(self)
