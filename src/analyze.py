import pandas as pd

def summarize_finances(df: pd.DataFrame) -> dict:
    income = df[df["amount"] > 0]["amount"].sum()
    spending = df[df["amount"] < 0]["amount"].sum()
    
    by_category = (
        df[df["amount"] < 0]
        .groupby("category")["amount"]
        .sum()
        .sort_values()
    )
    by_month = df.groupby("month")["amount"].sum().sort_index()

    return {
        "income": income,
        "spending": spending,
        "by_category": by_category,
        "by_month": by_month,
    }