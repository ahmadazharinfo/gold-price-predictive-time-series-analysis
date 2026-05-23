class CurrencyConverter:
    USD_RATE = 0.012  # Approximate INR → USD

    @staticmethod
    def inr_to_usd(value: float) -> float:
        return value * CurrencyConverter.USD_RATE
