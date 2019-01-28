import argparse
from dataclasses import fields

from dump import codecs
from hotel import Hotel
from parsing import parse_hotels, write_hotels

if __name__ == '__main__':
    extensions = ', '.join(codecs.keys())
    hotel_fields = {field.name for field in fields(Hotel)}

    parser = argparse.ArgumentParser(
        description='Parse hotel descriptions from csv and format them into several output formats [supported: {}]'.format(
            extensions))

    parser.add_argument('-i', '--input',
                        type=str,
                        help='The input csv file (example: hotels.csv)',
                        required=True)

    parser.add_argument('-o', '--output',
                        type=str,
                        help='The output file (example: converted_hotels.json) [supported: {}]'.format(extensions),
                        required=True)

    parser.add_argument('-s', '--sort',
                        type=str,
                        choices=hotel_fields,
                        help='Sort the hotels by field')

    parser.add_argument('-r', '--reverse',
                        action='store_true',
                        help='Sort the hotels in reverse order (only applies to --sort)')

    args = parser.parse_args()

    hotels = parse_hotels(args.input)

    if not hotels:
        print('The input csv file does not contain any valid hotels')
    else:
        if args.sort:
            hotels.sort(key=lambda hotel: hotel.asdict()[args.sort])

            if args.reverse:
                hotels.reverse()

        write_hotels(hotels, args.output)
