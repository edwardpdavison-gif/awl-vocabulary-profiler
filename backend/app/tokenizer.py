import re


def tokenize(text: str) -> list[str]:
    """
    Convert text into lowercase word tokens.
    """

    return re.findall(r"[a-zA-Z]+", text.lower())
