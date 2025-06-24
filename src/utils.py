import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    """
    Loads dataset CSV with 'url' and 'status' columns.

    status: 0 = phishing, 1 = legitimate
    """
    df = pd.read_csv(path)
    # Optionally, rename 'status' to 'label' or keep as is
    # Keep status as-is: 0=phish, 1=legit
    return df
