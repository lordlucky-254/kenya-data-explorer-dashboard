# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-23

### Added
- Modular architecture separating data loading (`src/data_loader.py`), analytics & SQL (`src/analytics.py`), visualizations (`src/charts.py`), and Streamlit UI (`src/app.py`).
- Interactive **Kenya County Map** with regional summary breakdown.
- **Correlations & Insights** tab with Pearson correlation matrix heatmap, OLS trendline on Rainfall vs. Maize Yield, and automated key findings.
- **Read-Only SQL Explorer** (in-memory SQLite) with preset queries and CSV export.
- Sidebar **Custom CSV Upload** with automatic schema validation.
- Unit test suite (`tests/`) covering data validation, KPIs, correlations, chart generation, and SQL query safety.
- GitHub Actions CI pipeline (`.github/workflows/ci.yml`) running `ruff` and `pytest`.
- Project governance and documentation: `LICENSE` (MIT), `CONTRIBUTING.md`, `data/DATA_DICTIONARY.md`, `pyproject.toml`, `.streamlit/config.toml`, and GitHub issue templates.

### Fixed
- Corrected repository directory layout (`data/kenya_dashboard.csv` and `src/app.py`) to match documentation and prevent `FileNotFoundError` on startup.
- Fixed M-Pesa Agents KPI to report latest-year total with year-over-year delta instead of double-counting agents across multiple years.
- Added graceful empty-state handling when no counties are selected.
- Removed internal scratch file `REPO_SETUP.md`.
