import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        # Read CSV
        df = pd.read_csv(self.file_path)
        
        # Remove empty rows (where Date is NaN)
        df = df.dropna(subset=['Date'])
        
        # Clean price column - remove commas and convert to float
        df['Price'] = df['Price'].str.replace(',', '').astype(float)
        
        # Parse dates in MMM-YY format
        # The format will interpret 'May-24' as May 2024 (not year 24 AD)
        df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')
        
        # Sort by date ascending (oldest first)
        df = df.sort_values('Date')
        
        # Keep only Date and Price columns
        df = df[['Date', 'Price']]
        
        return df
