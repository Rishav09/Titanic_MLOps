import pandas as pd
from hopsworks_client import get_hopsworks_client
from features import preprocess 

from config import RAW_DATA_PATH, PROCESSED_DATA_PATH


def main() -> None:
    df = pd.read_csv(RAW_DATA_PATH)
    df = preprocess(df)

    project = get_hopsworks_client()
    fs = project.get_feature_store()
    feature_group = fs.get_or_create_feature_group(
        name="titanic_features",
        version=1,
        primary_key=["PassengerId"],
        event_time="event_time",
        description="Preprocessed features for Titanic survival prediction",
    )
    feature_group.insert(df, write_options={"wait_for_job": True})

    print(f"Backfill completed. Saved to: Hopsworks feature group 'titanic_features' version 1.")
    fg = fs.get_feature_group(name="titanic_features", version=1)
    df_fg = fg.read()
    print(df_fg.head())
    print(df_fg.columns.tolist())
    print(df_fg.shape)


if __name__ == "__main__":
    main()