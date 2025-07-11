# COVID-19-Global-Dashboard
An interactive COVID-19 dashboard built using Dash, Plotly, and Pandas

---

## 📌 Overview

This project uses real-world COVID-19 data from **Our World in Data** to build an interactive dashboard for:
- Exploring new cases and deaths by country
- Tracking vaccination progress
- Enabling country-based filtering via dropdown

The app is built using the **Dash** framework (a Flask-based Python library for web apps) and visualized with **Plotly Express**.

---

## 🚀 Demo

Launch the dashboard locally:

```bash
python covid_dashboard.py
Then open your browser and go to:
http://127.0.0.1:8050/

| Tool   | Purpose                            |
| ------ | ---------------------------------- |
| Python | Core programming language          |
| Dash   | Web app framework for dashboard    |
| Plotly | Interactive graphing/visualization |
| Pandas | Data manipulation and cleaning     |
| CSV    | COVID-19 dataset format            |

📊 Data Source
Our World in Data – COVID-19 Dataset

covid-dashboard/
├── covid_dashboard.py     # Main app code
├── README.md              # Project overview
├── requirements.txt       # List of required libraries
└── owid-covid-data.csv    # Dataset (optional, or use a link)

💡 Features
Country selection dropdown

Daily new cases & deaths (line chart)

Cumulative vaccination data

Real-time interactive visualizations

👤 Author
David Jampana Abraham Luther
Email: davidabraham.jc@gmail.com
