import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

class ArimaConfig:
    def __init__(self, order=None, p=5, d=1, q=0):
        """
        Initialize ARIMA configuration.
        
        Args:
            order: Tuple of (p, d, q) values (takes precedence if provided)
            p: AR order (autoregressive)
            d: Differencing order
            q: MA order (moving average)
        """
        if order is not None:
            self.order = order
        else:
            self.order = (p, d, q)