import pandas as pd

def load_transactions(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)