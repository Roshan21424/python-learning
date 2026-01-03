import re
"""
regular expression:
regex is used to search, match, extract, or replace patterns in text
python provides the 're' module for regex operations
"""


# [A-Z]+ -> one or more uppercase letters
# \w+ -> one or more word characters (letters, digits, underscore)
pattern = r"[A-Z]+\w+"

text = """
a regular expression or RegEx is a special sequence of characters that uses a search pattern.
It can detect the presence or absence of a text.
regex module in python.
"""

def find_matches(pattern, text):

    return re.findall(pattern, text)


if __name__ == "__main__":
    matches = find_matches(pattern, text)
    print("Matches found:", matches)



def find_occurrences():
    """find all occurrences of a substring using regex."""
    text = "car ar bar market"
    matches = re.findall(r"ar", text)
    print("Occurrences of 'ar':", matches)


def replace_text():
    """replace characters in a string using regex."""
    text = "hello bye"
    result = re.sub(r"e", "0", text)
    print("After replacement:", result)


def split_text():
    """split a string based on a regex pattern."""
    text = "The rain in Spain"
    result = re.split(r"\s+", text)
    print("Split result:", result)


if __name__ == "__main__":
    find_occurrences()
    replace_text()
    split_text()
