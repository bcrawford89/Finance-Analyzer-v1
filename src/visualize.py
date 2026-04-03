import matplotlib.pyplot as plt
import pandas as pd


def plot_spending_by_category(df: pd.DataFrame) -> None:
    spending_by_category = (
        df[df["amount"] < 0]
        .groupby("category")["amount"]
        .sum()
        .abs()
        .sort_values(ascending=False)
    )

    if spending_by_category.empty:
        print("No spending data available to plot.")
        return

    plt.figure(figsize=(10, 6))
    spending_by_category.plot(kind="bar")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()