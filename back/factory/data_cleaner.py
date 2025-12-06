import pandas as pd 

class DataCleaner:
    @staticmethod
    def clean(file_path):
        df = pd.read_csv(file_path)
        df = df.dropna()
        return df