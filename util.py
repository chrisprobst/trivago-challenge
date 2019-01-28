import unicodedata


def is_printable(s):
    """
    :param s:
    The string to check.
    :return:
    True if the given string does not contain any control characters, otherwise False.
    """
    # Define unprintable characters based on the unicode category Cc
    # https://www.fileformat.info/info/unicode/category/index.htm
    return not any(unicodedata.category(c) == 'Cc' for c in s.strip())
