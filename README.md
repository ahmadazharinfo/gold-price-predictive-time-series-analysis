# Gold Price Prediction System

**University of Basrah — College of Engineering — Department of Computer Engineering**

**Supervised by:** Dr. Ali Nabeel  
**Team:**
- Ahmad Azhar Almansoor (1)
- Mohammed Saddam Yacoub (60)
- Hussain Zuhir Kadhim (15)
- Ali Amer Ibrahim (49)
- Ibrahim Madian Fadhil (92)

---

## Project Overview

A desktop application for forecasting gold prices using **ARIMA time-series modeling** on historical economic data including inflation rates, exchange rates, and oil prices. Built following the complete software engineering lifecycle: requirements analysis, UML modeling, layered MVC architecture, and SOLID/OOP design principles.

The system delivers monthly gold price forecasts for any future year through a Tkinter GUI, with exportable prediction tables and charts.

---

## Repository Structure

```
GoldPricePredictionProject/
│
├── main.py                      # Application entry point — orchestrates all components
├── config.py                    # System-wide configuration (paths, ARIMA params, GUI settings)
├── requirements.txt             # Python dependencies
│
├── Core Application — 10 OOP Classes
│   ├── data_loader.py           # DataLoader       — loads CSV data from disk
│   ├── data_preprocessor.py     # DataPreprocessor — cleans and prepares time-series data
│   ├── model_trainer.py         # ModelTrainer     — trains and serializes ARIMA model
│   ├── predictor.py             # Predictor        — generates monthly/yearly forecasts
│   ├── validator.py             # Validator        — validates user input and data integrity
│   ├── model_manager.py         # ModelManager     — coordinates full model lifecycle
│   ├── results_formatter.py     # ResultsFormatter — formats and exports prediction results
│   ├── gui_controller.py        # GUIController    — business logic layer between GUI and model
│   └── gui_app.py               # GoldPricePredictionGUI — Tkinter presentation layer
│
├── Utilities
│   ├── generate_sample_data.py  # Generates synthetic gold price CSV for testing
│   └── quick_start.py           # Automated setup and first-run script
│
├── Documentation
│   ├── README.md                # This file
│   ├── ARCHITECTURE.md          # Full layered architecture and component diagrams
│   ├── USER_GUIDE.md            # Step-by-step user instructions
│   └── PROJECT_SUMMARY.md       # Project deliverables overview
│
├── data/                        # Created automatically on first run
│   └── gold_prices.csv          # Gold price dataset (place here after download)
│
├── models/                      # Created automatically on first run
│   └── arima_model.pkl          # Serialized trained ARIMA model
│
└── Project Documents/
    ├── Gold_Price_Prediction_Project.pdf      # Requirements & Use-Case Specification
    └── GoldPricePredictionProject_Report.pdf  # Full technical report with UML diagrams
```

---

## Architecture

The system follows a **4-layer MVC architecture** ensuring modularity, scalability, and maintainability:

```
┌─────────────────────────────────────────┐
│         Presentation Layer              │
│         GoldPricePredictionGUI          │  ← gui_app.py
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│           Controller Layer              │
│           GUIController                 │  ← gui_controller.py
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│         Business Logic Layer            │
│   ModelManager · Validator ·            │  ← model_manager.py
│   ResultsFormatter                      │    validator.py
└──────────────────┬──────────────────────┘    results_formatter.py
                   │
┌──────────────────▼──────────────────────┐
│       Data / Model Layer                │
│   DataLoader · DataPreprocessor ·       │  ← data_loader.py
│   ModelTrainer · Predictor              │    data_preprocessor.py
└──────────────────┬──────────────────────┘    model_trainer.py
                   │                           predictor.py
            gold_prices.csv
```

---

## Class Responsibilities

| Class | File | Responsibility | OOP Principle |
|---|---|---|---|
| `Config` | `config.py` | System-wide constants and paths | High Cohesion — no dependencies |
| `DataLoader` | `data_loader.py` | Load CSV from disk | Low Coupling — depends only on Config |
| `DataPreprocessor` | `data_preprocessor.py` | Clean and prepare time-series data | Encapsulation of data cleaning logic |
| `ModelTrainer` | `model_trainer.py` | Train and persist ARIMA model | Single Responsibility |
| `Predictor` | `predictor.py` | Generate monthly/yearly forecasts | Abstraction — hides ARIMA internals |
| `Validator` | `validator.py` | Validate input and data integrity | Static utility — no state |
| `ModelManager` | `model_manager.py` | Orchestrate model lifecycle | Composition over inheritance |
| `ResultsFormatter` | `results_formatter.py` | Format and export results | Static utility — no state |
| `GUIController` | `gui_controller.py` | Business logic between GUI and model | Low Coupling — MVC Controller |
| `GoldPricePredictionGUI` | `gui_app.py` | Tkinter interface and user events | Encapsulation of all UI logic |

---

## OOP Design Principles Applied

**Encapsulation** — Each class hides its internal state and exposes only what is needed. `ModelTrainer` manages ARIMA fitting internally; callers only see `train()` and `save()`.

**Abstraction** — `Predictor` abstracts away ARIMA forecasting complexity. The GUI layer never interacts directly with statsmodels.

**Polymorphism** — `GUIController` works with model components through consistent interfaces, making it easy to swap ARIMA for LSTM or Prophet without changing the controller.

**High Cohesion / Low Coupling** — Each class has one responsibility. Communication flows through well-defined interfaces: `GUI → GUIController → ModelManager → {Data + Model classes}`.

**SOLID Principles** — Single Responsibility across all 10 classes; Open/Closed (new models can be added without modifying existing classes); Dependency Inversion (controller depends on abstractions, not concrete implementations).

---

## Installation & Setup

### Step 1 — Install Python 3.7+
Download from [python.org](https://www.python.org/) and make sure to check **"Add Python to PATH"** during installation.

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

Installs: `pandas` · `numpy` · `statsmodels` · `matplotlib` · `python-dateutil`

### Step 3 — Get the dataset

**Option A — Real dataset (recommended):**
1. Download from [Kaggle — Gold Price Prediction with Time Series Analysis](https://www.kaggle.com/datasets/harshjaglan01/gold-price-prediction-with-time-series-analysis)
2. Place the CSV file in the `data/` folder and rename it `gold_prices.csv`

**Option B — Sample data (for testing):**
```bash
python generate_sample_data.py
```

### Step 4 — Run the application
```bash
python main.py
```

Or use the automated setup script which handles everything:
```bash
python quick_start.py
```

---

## Usage

1. **Enter Year** — type a year (2026 or later) in the input field
2. **Generate Prediction** — click the button to run ARIMA forecasting
3. **View Results** — monthly predictions and yearly average are displayed in the results panel
4. **Export** — save predictions to a `.txt` file
5. **Retrain** — if you update the dataset, retrain the model from the GUI

---

## Dataset

| Property | Value |
|---|---|
| Source | Kaggle — Gold Price Prediction with Time Series Analysis |
| Format | CSV with `Date` and `Price` columns |
| Location | `data/gold_prices.csv` |
| Purpose | Historical gold prices for ARIMA time-series training |

Economic indicators used in analysis: inflation rates (CPI), US Dollar Index (DXY), crude oil prices, interest rates (FED data), S&P 500, NASDAQ Composite.

---

## UML Diagrams

All UML diagrams are documented in the technical report (`GoldPricePredictionProject_Report.pdf`):

- **Use Case Diagram** — 4-phase system flow (Data Verification → Model Training → Prediction → Export)
- **Class Diagram** — 10 classes with attributes, methods, and relationships
- **Sequence Diagram** — complete Generate Prediction flow across all components

---

## Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
statsmodels>=0.13.0
matplotlib>=3.4.0
python-dateutil>=2.8.0
```

---

## Tech Stack

`Python 3.7+` · `ARIMA (statsmodels)` · `Tkinter` · `pandas` · `numpy` · `pickle` · `OOP` · `MVC` · `UML`

---

## Disclaimer

This project is developed for academic purposes as a graduation project submission at the University of Basrah, 2024–2025.
