import pandas as pd
from pathlib import Path


DATA_PATH = Path(__file__).parent.parent / "data" / "awl_mvp_profiler.csv"


def load_awl_data():
    df = pd.read_csv(DATA_PATH)

    awl_lookup = {}

    for _, row in df.iterrows():
        match_form = str(row["match_form"]).lower()

        awl_lookup[match_form] = {
            "headword": row["headword"],
            "sublist": int(row["sublist"]),
            "family_id": row["family_id"]
        }

    return awl_lookup