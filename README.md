# Gold Price Prediction

A desktop application that forecasts monthly gold prices using an **ARIMA** (AutoRegressive Integrated Moving Average) time-series model. Built with Python and Tkinter.

---

## Features

- **ARIMA Forecasting** — predicts monthly gold prices for any future year (2026 +).
- **Dual Currency Display** — shows predictions in both INR and USD.
- **Monthly Breakdown** — 12-month forecast with per-month detail.
- **Summary Statistics** — average, highest, and lowest predicted prices.
- **Dark-Themed GUI** — premium Tkinter interface with gold accents.

---

## Project Structure

```
GoldPricePrediction/
├── data/
│   └── GoldPriceDataset.csv      # Historical gold price data
├── gui/
│   ├── __init__.py
│   ├── main_window.py            # Tkinter GUI (dark theme)
│   └── prediction_formatter.py   # Formats predictions for display
├── model/
│   ├── __init__.py
│   ├── arima_config.py           # ARIMA hyperparameters (p, d, q)
│   ├── arima_model.py            # ARIMA training & forecasting
│   ├── data_loader.py            # CSV loading & parsing
│   └── data_preprocessor.py      # Time-series preprocessing
├── utils/
│   ├── __init__.py
│   ├── currency_converter.py     # INR → USD conversion
│   ├── data_validator.py         # Input validation
│   └── prediction_service.py     # Orchestrates model predictions
├── main.py                       # Application entry point
├── main.ipynb                    # Jupyter notebook (development)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.10 or higher
- Tkinter (included with most Python installations)

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/GoldPricePrediction.git
cd GoldPricePrediction

# Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

1. Enter a target year (**2026** or later) in the input field.
2. Click **PREDICT ▸** or press **Enter**.
3. View the monthly forecast, currency conversions, and summary statistics.

---

## How It Works

| Step | Component | Description |
|------|-----------|-------------|
| 1 | `DataLoader` | Reads and cleans the CSV dataset |
| 2 | `DataPreprocessor` | Sets date index and monthly frequency |
| 3 | `ArimaModel` | Trains an ARIMA(1,1,1) model on the series |
| 4 | `PredictionService` | Calculates forecast steps for the target year |
| 5 | `PredictionFormatter` | Formats results into a readable table |
| 6 | `MainWindow` | Displays everything in a dark-themed GUI |

---

## Dataset

The dataset (`data/GoldPriceDataset.csv`) contains monthly average gold prices in INR. Date range covers historical data through May 2024.

---

## License

This project is provided for educational purposes.
