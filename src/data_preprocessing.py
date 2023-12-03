import src.data_ingestion as di

dii = di.DataIngestion()
path = 'data/sample.csv'

data = dii.get_data()

class DataCleaning():
    def __init__():
        pass

    def handle_nan(data:pd.DataFrame) -> pd.DataFrame:
        data = data.dropna()
        # future staff