def print_upper_words(words):
    """Print each word on  a separate line, upppercased

        >>> print_upper_words(["i", "am", "extrememly", "tired"])
        I
        AM
        EXTREMELY
        TIRED
    """

    for word in words:
        print(word.upper())