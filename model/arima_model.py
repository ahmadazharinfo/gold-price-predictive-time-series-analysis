import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from .arima_config import ArimaConfig


class ArimaModel:
    def __init__(self, config: ArimaConfig):
        self.config = config
        self.model_fit = None

    def train(self, series):
        model = ARIMA(series, order=self.config.order)
        self.model_fit = model.fit()

    def forecast(self, steps):
        if self.model_fit is None:
            raise RuntimeError("Model must be trained before forecasting")
        return self.model_fit.forecast(steps=steps)
