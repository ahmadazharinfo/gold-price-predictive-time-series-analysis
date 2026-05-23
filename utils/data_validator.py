class DataValidator:
    @staticmethod
    def validate_year(year: int):
        if year < 2026:
            raise ValueError("Year must be 2026 or later")
    
    @staticmethod
    def validate_positive(value: float, name: str = "Value"):
        if value < 0:
            raise ValueError(f"{name} must be positive")