import unicodedata


def is_printable(s):
    # Define unprintable characters based on the unicode category Cc
    # https://www.fileformat.info/info/unicode/category/index.htm
    return not any(unicodedata.category(c) == 'Cc' for c in s.strip())
