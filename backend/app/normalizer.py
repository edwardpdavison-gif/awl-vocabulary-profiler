from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


def get_candidate_forms(token: str) -> list[str]:
    token = token.lower()

    candidates = [
        token,
        lemmatizer.lemmatize(token, pos="v"),
        lemmatizer.lemmatize(token, pos="n"),
        lemmatizer.lemmatize(token, pos="a"),
        lemmatizer.lemmatize(token, pos="r"),
    ]

    return list(dict.fromkeys(candidates))