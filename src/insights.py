import pandas as pd

def generate_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    spending_df = df[df["amount"] < 0].copy()
    income_total = df[df["amount"] > 0]["amount"].sum()
    spending_total = abs(spending_df["amount"].sum())

    if not spending_df.empty:
        top_category = (
            spending_df.groupby("category")["amount"]
            .sum()
            .sort_values()
            .index[0]
        )
        insights.append(f"Highest spending category: {top_category}")

    monthly_spending = (
        spending_df.groupby("month")["amount"]
        .sum()
        .sort_values()
    )
    if not monthly_spending.empty:
        worst_month = monthly_spending.index[0]
        insights.append(f"Highest spending month: {worst_month}")

    if spending_total > income_total:
        insights.append("Warning: spending exceeded income for this dataset.")

    subscription_keywords = ["NETFLIX", "SPOTIFY", "HULU", "DISNEY", "APPLE", "Blizzard Entertainment"]
    subscription_spend = spending_df[
        spending_df["description"].str.upper().str.contains("|".join(subscription_keywords), na=False)
    ]["amount"].sum()

    if subscription_spend < 0:
        insights.append(f"Estimated subscription spending: ${abs(subscription_spend):.2f}")

    return insights