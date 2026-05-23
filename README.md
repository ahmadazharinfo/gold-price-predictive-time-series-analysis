# Gold Price Prediction System

**University of Basrah - College of Engineering - Department of Computer Engineering**

**Supervised by:** Dr. Ali Nabeel  
**Team:**
- Ahmad Azhar Almansoor (1)
- Mohammed Saddam Yacoub (60)
- Hussain Zuhir Kadhim (15)
- Ali Amer Ibrahim (49)
- Ibrahim Madian Fadhil (92)

---

## Overview

A Tkinter desktop application that forecasts monthly gold prices using **ARIMA time-series modeling** on historical INR gold price data. The user enters a target year (2026 or later) and receives a full 12-month forecast in both **INR and USD**, along with a summary of the yearly average, highest, and lowest predicted months.

The project follows the complete software engineering lifecycle - requirements analysis, UML modeling (Use Case, Class, Sequence diagrams), layered MVC architecture, and SOLID/OOP design principles.

---

## Project Structure

```
GoldPricePrediction/
│
├── main/
│   ├── main.py               # GoldPriceApp - entry point, wires all components
│   └── main.ipynb            # Jupyter notebook version for exploration
│
├── model/                    # ML layer — data handling and ARIMA model
│   ├── __init__.py
│   ├── arima_config.py       # ArimaConfig       - stores (p, d, q) order
│   ├── arima_model.py        # ArimaModel        - trains and forecasts with ARIMA
│   ├── data_loader.py        # DataLoader        - reads and parses GoldPriceDataset.csv
│   └── data_preprocessor.py  # DataPreprocessor  - sets DatetimeIndex, forward-fills gaps
│
├── utils/                    # Business logic layer
│   ├── __init__.py
│   ├── prediction_service.py # PredictionService - computes forecasts per target year
│   ├── currency_converter.py # CurrencyConverter - converts INR → USD (static utility)
│   └── data_validator.py     # DataValidator     - validates year and numeric inputs
│
├── gui/                      # Presentation layer
│   ├── __init__.py
│   ├── main_window.py        # MainWindow        - dark-themed Tkinter UI (560×740)
│   └── prediction_formatter.py # PredictionFormatter - formats results as text table
│
├── data/
│   └── GoldPriceDataset.csv  # 240 months of INR gold prices (May 2004 → May 2024)
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Architecture

The system follows a **3-layer MVC architecture**:

```
┌──────────────────────────────────────┐
│          Presentation Layer          │
│  MainWindow · PredictionFormatter    │   ← gui/
└──────────────────┬───────────────────┘
                   │  callback (on_predict)
┌──────────────────▼───────────────────┐
│         Business Logic Layer         │
│  PredictionService                   │   ← utils/
│  DataValidator · CurrencyConverter   │
└──────────────────┬───────────────────┘
                   │
┌──────────────────▼───────────────────┐
│           ML / Data Layer            │
│  DataLoader · DataPreprocessor       │   ← model/
│  ArimaConfig · ArimaModel            │
└──────────────────┬───────────────────┘
                   │
           GoldPriceDataset.csv
```

**Entry point** - `GoldPriceApp` in `main/main.py` instantiates and wires all layers:

```
GoldPriceApp
 ├── DataLoader          → loads CSV
 ├── DataPreprocessor    → cleans & indexes the time series
 ├── ArimaModel(ArimaConfig(p=1, d=1, q=1)) → trains on historical data
 ├── PredictionService   → wraps model, computes year-specific forecasts
 └── MainWindow(root, _predict) → GUI with callback into GoldPriceApp._predict()
```

---

## Class Reference

### `model/` - ML & Data Layer

| Class | File | Responsibility |
|---|---|---|
| `ArimaConfig` | `arima_config.py` | Stores ARIMA `(p, d, q)` order; accepts either a tuple or individual `p`, `d`, `q` params |
| `ArimaModel` | `arima_model.py` | Wraps statsmodels ARIMA - `train(series)` fits the model, `forecast(steps)` returns predictions |
| `DataLoader` | `data_loader.py` | Reads CSV, strips commas from prices, parses `MMM-YY` dates, sorts ascending |
| `DataPreprocessor` | `data_preprocessor.py` | Sets `Date` as `DatetimeIndex` with monthly frequency (`MS`), forward-fills any gaps |

### `utils/` — Business Logic Layer

| Class | File | Responsibility |
|---|---|---|
| `PredictionService` | `prediction_service.py` | Calculates total forecast steps from dataset end (May 2024) to target year, returns last 12 months |
| `CurrencyConverter` | `currency_converter.py` | Static `inr_to_usd(value)` at a fixed rate (0.012 INR/USD) |
| `DataValidator` | `data_validator.py` | Static `validate_year(year)` - rejects years before 2026; `validate_positive(value, name)` |

### `gui/` — Presentation Layer

| Class | File | Responsibility |
|---|---|---|
| `MainWindow` | `main_window.py` | Dark-themed Tkinter window (560×740 px); year entry, Predict button, scrollable results panel, status indicator |
| `PredictionFormatter` | `prediction_formatter.py` | Static `format(predictions, converter)` - renders 12-month INR/USD table plus yearly summary (avg, high, low) |

---

## OOP Design Principles

**Encapsulation** - Each class manages its own state privately. `ArimaModel` holds `model_fit` internally; callers only use `train()` and `forecast()`. `MainWindow` keeps all widget references private.

**Abstraction** - `PredictionService.predict_year(year)` hides all step-counting arithmetic from the rest of the system. The GUI never touches `statsmodels` directly.

**Polymorphism** - `PredictionFormatter.format()` accepts any `converter` with an `inr_to_usd()` method, making it easy to swap `CurrencyConverter` for a live-rate implementation without changing the formatter.

**Single Responsibility** - Every class has exactly one job: `DataLoader` only loads, `DataPreprocessor` only preprocesses, `DataValidator` only validates, and so on.

**Low Coupling** - Layers communicate through clean interfaces. `GoldPriceApp` passes a callback (`_predict`) into `MainWindow` so the GUI never imports from `model/` or `utils/` directly.

**High Cohesion** - Each package (`model/`, `utils/`, `gui/`) groups only related classes with a focused, single purpose.

---

## Dataset

| Property | Value |
|---|---|
| File | `data/GoldPriceDataset.csv` |
| Columns | `Date` (MMM-YY format), `Price` (INR, comma-formatted) |
| Coverage | May 2004 → May 2024 (240 monthly records) |
| Source | Historical Indian gold prices |

The dataset is loaded, cleaned (commas stripped, dates parsed to `datetime`), sorted ascending, and converted to a monthly `DatetimeIndex` time series before ARIMA training.

---

## Installation

**Requirements:** Python 3.8+, tkinter (bundled with standard Python)

```bash
pip install -r requirements.txt
```

Dependencies:
```
pandas>=2.0.0
statsmodels>=0.14.0
```

---

## Running the Application

```bash
cd main
python main.py
```

Or open `main/main.ipynb` in Jupyter for the notebook version.

---

## Usage

1. **Launch** - run `python main/main.py`
2. **Enter year** - type any year from **2026 onwards** in the input field
3. **Predict** - click `PREDICT ▸` or press `Enter`
4. **Read results** - the scrollable panel shows a 12-month table with INR and USD prices, plus a summary

### Example output
```
  ◈  MONTHLY GOLD PRICE FORECAST
  ──────────────────────────────────────────────
  Month              INR              USD
  ──────────────────────────────────────────────
  January       85,412.30          1,024.95
  February      86,100.44          1,033.21
  ...
  December      91,120.88          1,093.45
  ──────────────────────────────────────────────

  ▲  SUMMARY
  Average       87,243.10 INR  |   1,046.92 USD
  Highest       91,120.88 INR  (December)
  Lowest        84,890.12 INR  (January)
```

---

## ARIMA Configuration

The model is initialized with `ArimaConfig(p=1, d=1, q=1)` in `main.py`. To experiment with different parameters:

```python
# In main/main.py - _setup_model()
self.model = ArimaModel(
    ArimaConfig(p=5, d=1, q=0)     # alternative order
)

# Or pass a tuple directly
ArimaConfig(order=(5, 1, 2))
```

---

## Tech Stack

`Python 3.8+` · `ARIMA (statsmodels)` · `Tkinter` · `pandas` · `OOP` · `MVC` · `UML`

---

## Disclaimer

Developed as an academic graduation project at the University of Basrah, 2024–2025. Predictions are based on historical patterns only and are not intended as financial advice.
