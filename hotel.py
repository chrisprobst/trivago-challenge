from dataclasses import dataclass, asdict

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
        - "address"
        - "stars" must be between 0 and 5 (incl.)
        - "contact"
        - "uri"

        :return:
        None if the hotel is totally valid, otherwise a string which contains the reason for the failed validation.
        """

        if not is_printable(self.name):
            return 'Name not printable ({})'.format(self.name)

        try:
            self.stars = int(self.stars)
            if not (0 <= self.stars <= 5):
                return 'Stars not between 0 and 5'
        except ValueError:
            return 'Stars "{}" cannot be parsed as int'.format(self.stars)

    def asdict(self):
        return asdict(self)
