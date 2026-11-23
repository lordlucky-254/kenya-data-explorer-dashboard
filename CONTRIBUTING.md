# Contributing to Kenya Data Explorer Dashboard

Thank you for your interest in improving this project! Contributions of all kinds—real Kenyan datasets, new visualizations, bug fixes, tests, and documentation—are welcome.

## Local Development Setup

```bash
git clone https://github.com/lordlucky-254/kenya-data-explorer-dashboard.git
cd kenya-data-explorer-dashboard

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -r requirements-dev.txt
```

## Running the App

```bash
streamlit run src/app.py
```

## Code Quality & Testing

Before opening a pull request, make sure linting and tests pass:

```bash
ruff check src tests
pytest
```

## Pull Request Guidelines

1. Create a focused branch (e.g., `feat/knbs-real-data` or `fix/map-tooltip`).
2. Keep business logic in `src/data_loader.py`, `src/analytics.py`, or `src/charts.py` so it can be unit-tested independently of Streamlit UI state.
3. Add or update unit tests under `tests/` for any behavioral changes.
4. Update `data/DATA_DICTIONARY.md` and `README.md` if you add columns or features.
