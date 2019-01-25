import csv
import json
from dataclasses import fields
from os.path import splitext

import dicttoxml

from hotel import Hotel


def dump_xml(data, f):
    b = dicttoxml.dicttoxml(data,
                            custom_root='hotels',
                            attr_type=False,
                            item_func=lambda _: 'hotel')
    f.write(b.decode('utf-8'))


def dump_csv(data, f):
    writer = csv.DictWriter(f, fieldnames=[field.name for field in fields(Hotel)])
    writer.writeheader()
    for d in data:
        writer.writerow(d)


# All allowed output codecs are stored here
# To support a new output codec, simply add a new entry which satisfies the following convention:
# 'extension' => lambda data, file_handle: ...
codecs = {
    '.json': json.dump,
    '.csv': dump_csv,
    '.xml': dump_xml,
}


def parse_hotels(cvs_path):
    """
    Parses a CSV file and creates a list of hotels out of it.
    Any parsing errors will be printed to stdout.

    :param cvs_path:
    A file path pointing to a CSV file for parsing hotels.
    :return:
    A list with successfully parsed rows (hotels), could also be empty if there are no rows or parsing failed at all.
    """

    hotels = []

    try:
        # Open CSV file with UTF-8 encoding (this also means that ONLY UTF-8 encoded files are accepted)
        with open(cvs_path, encoding='utf-8') as f:
            header = None

            # CSV files can contain empty rows
            non_empty_rows = (row for row in csv.reader(f) if row)

            for line, row in enumerate(non_empty_rows):
                # The first row is the header which specifies the order of the columns
                if not header:
                    header = row
                    continue

                # Zip column names with the current row and pass as dict to Hotel dataclass constructor,
                # so that even if the csv columns order change, the Hotel will be created correctly
                hotel = Hotel(**dict(zip(header, row)))

                reason = hotel.validate()

                if reason:
                    print('[Line {}] Invalid hotel found ({})'.format(line, reason))
                    continue

                hotels.append(hotel)
    except UnicodeDecodeError:
        print('CSV file "{}" is not a valid UTF-8 file'.format(cvs_path))

    return hotels


def write_hotels(hotels, path):
    _, ext = splitext(path)

    if ext not in codecs:
        print('Invalid output format "{}" (Supported formats are: {})'.format(ext, ', '.join(codecs.keys())))
        return

    codec = codecs[ext]
    hotels_as_dicts = [hotel.asdict() for hotel in hotels]

    with open(path, 'w', encoding='utf-8') as f:
        codec(hotels_as_dicts, f)
