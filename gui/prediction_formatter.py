class PredictionFormatter:
    """Formats monthly predictions into a visually structured text report."""

    @staticmethod
    def format(predictions, converter):
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        # Safety check: ensure we have exactly 12 predictions
        predictions_list = list(predictions)
        if len(predictions_list) != 12:
            return f"Error: Expected 12 monthly predictions, but got {len(predictions_list)}"

        divider = "  " + "\u2500" * 42 + "\n"
        text = ""

        text += "  \u25C8  MONTHLY GOLD PRICE FORECAST\n"
        text += divider
        text += f"  {'Month':<14} {'INR':>12}    {'USD':>10}\n"
        text += divider

        total_inr = 0
        high_val = float("-inf")
        low_val = float("inf")
        high_month = ""
        low_month = ""

        for i, value in enumerate(predictions_list):
            usd = converter.inr_to_usd(value)
            total_inr += value

            if value > high_val:
                high_val = value
                high_month = months[i]
            if value < low_val:
                low_val = value
                low_month = months[i]

            text += f"  {months[i]:<14} {value:>12,.2f}    {usd:>10,.2f}\n"

        avg_inr = total_inr / 12
        avg_usd = converter.inr_to_usd(avg_inr)
        high_usd = converter.inr_to_usd(high_val)
        low_usd = converter.inr_to_usd(low_val)

        text += divider
        text += "\n"
        text += "  \u25B2  SUMMARY\n"
        text += f"  Average    {avg_inr:>12,.2f} INR  |  {avg_usd:>10,.2f} USD\n"
        text += f"  Highest    {high_val:>12,.2f} INR  ({high_month})\n"
        text += f"  Lowest     {low_val:>12,.2f} INR  ({low_month})\n"

        return text
