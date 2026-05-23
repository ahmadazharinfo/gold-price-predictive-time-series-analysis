from datetime import datetime

class PredictionService:
    def __init__(self, model):
        self.model = model

    def predict_year(self, year: int):
        """
        Predict gold prices for a specific year.
        
        Args:
            year: The target year (e.g., 2026)
            
        Returns:
            List of 12 monthly predictions for that year
        """
        # Your data ends at May 2024 (month 5)
        last_data_year = 2024
        last_data_month = 5
        
        # Validate input
        if year < 2025:
            raise ValueError(f"Cannot predict for year {year}. Please choose 2025 or later.")
        
        # Calculate total months to forecast
        # From June 2024 to end of target year
        years_diff = year - last_data_year
        
        # Months from June 2024 to end of target year
        # = (remaining months in 2024) + (full years in between * 12) + (all 12 months of target year)
        remaining_in_2024 = 12 - last_data_month  # 7 months (Jun-Dec)
        full_years_between = max(0, years_diff - 1)  # Years between 2024 and target
        
        total_steps = remaining_in_2024 + (full_years_between * 12) + 12
        
        print(f"Debug: Forecasting {total_steps} steps for year {year}")
        
        # Get all predictions
        all_predictions = self.model.forecast(total_steps)
        
        print(f"Debug: Got {len(all_predictions)} predictions, extracting last 12")
        
        # Return only the last 12 months (the target year)
        result = list(all_predictions[-12:])
        
        print(f"Debug: Returning {len(result)} predictions")
        
        return result