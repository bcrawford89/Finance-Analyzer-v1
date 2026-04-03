from src.load_data import load_transactions
from src.clean_data import clean_transactions
from src.analyze import summarize_finances
from src.insights import generate_insights

def main() -> None:
    # Load transaction data
    df = load_transactions("data/sample_transactions.csv")
    # Clean transaction data
    df = clean_transactions(df)
    # Pull data summary and print
    summary = summarize_finances(df)
    print("\n=== Financial Summary ===\n")
    print(f"Total Income: ${summary['income']:.2f}")
    print(f"Total Spending: ${abs(summary['spending']):.2f}\n")

    print("Spending by Category:")
    for category, amount in summary["by_category"].items():
        print(f"  - {category}: ${abs(amount):.2f}")

    print("\nNet by Month:")
    for month, amount in summary["by_month"].items():
        print(f"  - {month}: ${amount:.2f}")
    # Create financial insights and print
    insights = generate_insights(df)
    print(insights)

if __name__ == "__main__":
    main()