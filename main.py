from src.load_data import load_transactions

def main() -> None:
    df = load_transactions("data/sample_transactions.csv")
    df = clean_transactions(df)
    print(df.head())

if __name__ == "__main__":
    main()