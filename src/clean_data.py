import pandas as pd

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # Clean up money signs to create raw number values for dataframe
    df["amount"] = (
        df["amount"]
        .astype(str)
        .str.replace("$","" , regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["category"] = df["category"].fillna("Other")
    df["month"] = df["date"].dt.to_period("M").astype(str)
    df = df.dropna(subset=["date", "amount"])
    return df