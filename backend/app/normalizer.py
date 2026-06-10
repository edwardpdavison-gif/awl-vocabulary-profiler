def simple_lemma(token: str) -> str:
    word = token.lower()

    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"

    if word.endswith("ing") and len(word) > 5:
        base = word[:-3]
        if len(base) >= 2 and base[-1] == base[-2]:
            base = base[:-1]
        return base

    if word.endswith("ed") and len(word) > 4:
        base = word[:-2]
        if len(base) >= 2 and base[-1] == base[-2]:
            base = base[:-1]
        return base

    if word.endswith("s") and len(word) > 3:
        return word[:-1]

    return word


def get_candidate_forms(token: str) -> list[str]:
    word = token.lower()
    lemma = simple_lemma(word)

    candidates = [word]

    if lemma != word:
        candidates.append(lemma)

    return candidates