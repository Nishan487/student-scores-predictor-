from factory.data_cleaner import DataCleaner
from factory.predictor import Predictor
from factory.model_trainer import ModelTrainer
from factory.plotter import Plotter
import pandas as pd

class Processing:
    @staticmethod
    def process(file_path,hours):
        df = DataCleaner.clean(file_path)
        df = pd.DataFrame(df)
        Plotter.plot(df)
        model = ModelTrainer.train(df)
        predicted_score = Predictor.predict(model, hours)
        print(f"Predicted score for studying {hours} hours: {predicted_score}")
        return predicted_score
    
    