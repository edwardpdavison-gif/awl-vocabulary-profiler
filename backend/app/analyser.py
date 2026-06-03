def analyse_text_against_awl(text: str, awl_lookup: dict, tokenize) -> dict:

    tokens = tokenize(text)

    awl_token_count = 0
    matched_families = set()
    matched_word_counts = {}
    sublist_breakdown = {}

    for token in tokens:

        if token in awl_lookup:

            entry = awl_lookup[token]

            awl_token_count += 1
            matched_families.add(entry["family_id"])

            if token not in matched_word_counts:
                matched_word_counts[token] = {
                    "word": token,
                    "headword": entry["headword"],
                    "sublist": entry["sublist"],
                    "frequency": 0
                }

            matched_word_counts[token]["frequency"] += 1

            sublist = str(entry["sublist"])

            if sublist not in sublist_breakdown:
                sublist_breakdown[sublist] = 0

            sublist_breakdown[sublist] += 1

    awl_percentage = 0.0

    if len(tokens) > 0:
        awl_percentage = float(round((awl_token_count / len(tokens)) * 100, 2))

    return {
        "total_words": len(tokens),
        "awl_token_count": awl_token_count,
        "awl_family_count": len(matched_families),
        "awl_percentage": awl_percentage,
        "matched_words": list(matched_word_counts.values()),
        "sublist_breakdown": sublist_breakdown
    }