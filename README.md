# 📊 Kenya Data Explorer Dashboard

> Interactive dashboard for Kenyan data — rainfall vs maize yield, KCSE scores, house prices, M-Pesa agents. Turn data into decisions.

**Author:** lucky vincent — [@lordlucky-254](https://github.com/lordlucky-254) | Karatina University | Data/AI
**Stack:** Python • Pandas • Streamlit • Plotly

## What it does
Explore Kenya by county & year:
- Rainfall vs Maize Yield — does more rain = more yield?
- KCSE mean scores by county over time
- House prices by county
- M-Pesa agents vs economic activity

## Dataset
`data/kenya_dashboard.csv` — 80 rows (10 counties x 8 years 2018-2025), synthetic but realistic.
Columns: `county, year, rainfall_mm, maize_yield_tonnes_per_ha, kcse_mean_score, house_price_ksh, mpesa_agents`

## How to run it
```bash
git clone https://github.com/lordlucky-254/kenya-data-explorer-dashboard.git
cd kenya-data-explorer-dashboard
pip install -r requirements.txt
streamlit run src/app.py
```

## Project structure
```
kenya-data-explorer-dashboard/
├── data/kenya_dashboard.csv
├── src/app.py
├── README.md
└── requirements.txt
```

## What I learned
- Data storytelling: filters, KPIs, and charts that answer a question — not just plots
- How to build a Streamlit dashboard that a non-technical person can use
- Correlation vs causation: rainfall helps yield, but not alone

## Next steps
- [ ] Replace with real KNBS / World Bank Kenya data
- [ ] Add SQL + download filtered CSV button
- [ ] Add map of counties

## Tech
Python • Pandas • Streamlit • Plotly
