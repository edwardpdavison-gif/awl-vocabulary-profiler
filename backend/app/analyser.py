from app.normalizer import get_candidate_forms


def analyse_text_against_awl(
    text: str,
    awl_lookup: dict,
    gsl_lookup: dict,
    tokenize
) -> dict:

    tokens = tokenize(text)

    awl_token_count = 0
    gsl_token_count = 0
    offlist_token_count = 0

    awl_families = set()

    matched_awl_words = {}
    matched_gsl_words = {}

    awl_sublist_breakdown = {}

    for token in tokens:

        candidate_forms = get_candidate_forms(token)

        awl_match = None
        gsl_match = None

        # AWL takes priority
        for form in candidate_forms:
            if form in awl_lookup:
                awl_match = {
                    "form": form,
                    "entry": awl_lookup[form]
                }
                break

        if awl_match is not None:

            matched_form = awl_match["form"]
            entry = awl_match["entry"]

            awl_token_count += 1
            awl_families.add(entry["family_id"])

            if matched_form not in matched_awl_words:
                matched_awl_words[matched_form] = {
                    "word": matched_form,
                    "headword": entry["headword"],
                    "sublist": entry["sublist"],
                    "frequency": 0
                }

            matched_awl_words[matched_form]["frequency"] += 1

            sublist = str(entry["sublist"])

            if sublist not in awl_sublist_breakdown:
                awl_sublist_breakdown[sublist] = 0

            awl_sublist_breakdown[sublist] += 1

            continue

        for form in candidate_forms:
            if form in gsl_lookup:
                gsl_match = {
                    "form": form,
                    "entry": gsl_lookup[form]
                }
                break

        if gsl_match is not None:

            matched_form = gsl_match["form"]
            entry = gsl_match["entry"]

            gsl_token_count += 1

            if matched_form not in matched_gsl_words:
                matched_gsl_words[matched_form] = {
                    "word": matched_form,
                    "headword": entry["headword"],
                    "frequency": 0
                }

            matched_gsl_words[matched_form]["frequency"] += 1

            continue

        offlist_token_count += 1

    total_words = len(tokens)

    awl_percentage = 0.0
    gsl_percentage = 0.0
    offlist_percentage = 0.0

    if total_words > 0:

        awl_percentage = round(
            (awl_token_count / total_words) * 100,
            2
        )

        gsl_percentage = round(
            (gsl_token_count / total_words) * 100,
            2
        )

        offlist_percentage = round(
            (offlist_token_count / total_words) * 100,
            2
        )

    return {
        "total_words": total_words,

        "awl_token_count": awl_token_count,
        "gsl_token_count": gsl_token_count,
        "offlist_token_count": offlist_token_count,

        "awl_percentage": awl_percentage,
        "gsl_percentage": gsl_percentage,
        "offlist_percentage": offlist_percentage,

        "awl_family_count": len(awl_families),

        "matched_awl_words": list(
            matched_awl_words.values()
        ),

        "matched_gsl_words": list(
            matched_gsl_words.values()
        ),

        "awl_sublist_breakdown": awl_sublist_breakdown,

        "profile_breakdown": {
            "AWL": awl_token_count,
            "GSL": gsl_token_count,
            "Off-list": offlist_token_count
        }
    }
