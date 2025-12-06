import pandas as pd

class Predictor:
    @staticmethod
    def predict(model, hours):
        df=pd.DataFrame({'Hours':[hours]})
        return model.predict(df)[0]