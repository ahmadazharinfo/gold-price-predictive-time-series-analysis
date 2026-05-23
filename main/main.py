import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import tkinter as tk
from model import DataLoader, DataPreprocessor, ArimaConfig, ArimaModel
from utils import DataValidator, CurrencyConverter, PredictionService
from gui import MainWindow, PredictionFormatter


class GoldPriceApp:
    def __init__(self):
        self._setup_model()
        self._setup_gui()

    def _setup_model(self):
        # Use relative path to find the CSV alongside this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, "data", "GoldPriceDataset.csv")

        loader = DataLoader(csv_path)
        df = loader.load()

        preprocessor = DataPreprocessor()
        series = preprocessor.preprocess(df)

        self.model = ArimaModel(
            ArimaConfig(p=1, d=1, q=1)
        )
        self.model.train(series)

        self.prediction_service = PredictionService(self.model)

    def _setup_gui(self):
        self.root = tk.Tk()
        self.window = MainWindow(self.root, self._predict)

    def _predict(self, year):
        try:
            DataValidator.validate_year(year)
            predictions = self.prediction_service.predict_year(year)
            predictions_list = list(predictions)
            result = PredictionFormatter.format(predictions_list, CurrencyConverter)
            return result
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            return f"Error: {e}\n\n{error_details}"

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = GoldPriceApp()
    app.run()
