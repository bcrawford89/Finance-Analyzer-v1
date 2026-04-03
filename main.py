from src.load_data import load_transactions
from src.clean_data import clean_transactions
from src.analyze import summarize_finances
from src.insights import generate_insights
from src.visualize import plot_spending_by_category

def main() -> None:
    # Load transaction data
    file_path = "data/sample_transactions.csv"
    df = load_transactions(file_path)
    # Clean transaction data
    df = clean_transactions(df)
    # Helper functions
    summary = summarize_finances(df)
    insights = generate_insights(df)
    # Pull data summary and print
    print("\n=== Financial Summary ===\n")
    print(f"Source file: {file_path}\n")
    print(f"Total Income: ${summary['income']:.2f}")
    print(f"Total Spending: ${abs(summary['spending']):.2f}\n")

    print("Spending by Category:")
    for category, amount in summary["by_category"].items():
        print(f"  - {category}: ${abs(amount):.2f}")

    print("\nNet by Month:")
    for month, amount in summary["by_month"].items():
        print(f"  - {month}: ${amount:.2f}")
    
    # Create financial insights and print
    print("\nInsights:")
    if insights:
        for insight in insights:
            print(f"  - {insight}")
    else:
        print("  - No insights available.")
    
    # Print spending chart by category
    plot_spending_by_category(df)

if __name__ == "__main__":
    main()