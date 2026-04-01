import pandas as pd


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = [col.strip() for col in df.columns]

    selected_cols = [
        "passengerid",
        "sex",
        "age",
        "pclass",
        "fare",
        "parch",
        "sibsp",
        "embarked",
        "survived",
    ]
    df = df[selected_cols]

    fill_values = {
        "age": df["age"].mean(),
        "embarked": df["embarked"].mode()[0],
    }
    df = df.fillna(fill_values)

    df["family_size"] = df["sibsp"] + df["parch"] + 1
    df["is_alone"] = (df["family_size"] == 1).astype(int)
    df["event_time"] = pd.Timestamp.now()

    return df