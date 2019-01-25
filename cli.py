from parsing import parse_hotels, write_hotels

if __name__ == '__main__':
    hotels = parse_hotels('./hotels2.csv')
    write_hotels(hotels, './hotels3.xml')
