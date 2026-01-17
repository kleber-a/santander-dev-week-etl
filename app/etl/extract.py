import pandas as pd

class Extract:
    @staticmethod
    def from_csv(path: str) -> pd.DataFrame:
        return pd.read_csv(path)
