import pandas as pd

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["category"] = df["category"].fillna("Uncategorized")
    df["month"] = df["date"].dt.to_period("M").astype(str)
    df = df.dropna(subset=["date", "amount"])
    return df