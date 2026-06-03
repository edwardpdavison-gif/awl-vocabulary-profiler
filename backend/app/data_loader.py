import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent / "data"

AWL_DATA_PATH = DATA_DIR / "awl_mvp_profiler.csv"
GSL_DATA_PATH = DATA_DIR / "gsl_mvp_profiler.csv"


def load_awl_data():
    df = pd.read_csv(AWL_DATA_PATH)

    awl_lookup = {}

    for _, row in df.iterrows():
        match_form = str(row["match_form"]).lower()

        awl_lookup[match_form] = {
            "headword": row["headword"],
            "sublist": int(row["sublist"]),
            "family_id": row["family_id"]
        }

    return awl_lookup


def load_gsl_data():
    df = pd.read_csv(GSL_DATA_PATH)

    gsl_lookup = {}

    for _, row in df.iterrows():
        match_form = str(row["match_form"]).lower()

        gsl_lookup[match_form] = {
            "headword": row["headword"],
            "list_name": row["list_name"],
            "gsl_rank": int(row["gsl_rank"]),
            "family_id": row["family_id"]
        }

    return gsl_lookup