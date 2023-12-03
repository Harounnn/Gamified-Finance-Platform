import pandas as pd


class DataIngestion():
    def get_data(path: str) -> pd.DataFrame :
        data = pd.read_csv('path')
        return data