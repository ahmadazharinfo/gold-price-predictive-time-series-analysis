import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

class DataPreprocessor:
    def preprocess(self, df):
        # Set Date as index
        df = df.set_index('Date')
        
        # Set monthly start frequency
        df = df.asfreq('MS')
        
        # Forward fill missing values (updated method)
        df = df.ffill()
        
        # Return the Price series
        return df['Price']
