README.md
✈️ Flight Activity Tracker

Analyze peak flight activity by location using real-world aviation data
📌 Overview

Flight Activity Tracker is a data engineering project that ingests, processes, and analyzes flight data to identify peak traffic times at various airports. The project demonstrates a real-world data pipeline using Python, PostgreSQL, and SQL, with interactive visualizations for time-based and location-based traffic patterns.
🚀 Features

    Collects real or historical flight data (e.g. via OpenSky API)

    Stores data in a relational database (PostgreSQL)

    Aggregates and analyzes traffic per airport and time window

    Interactive dashboard (Streamlit or Jupyter) for exploring peak activity

    Optional geospatial visualization using Plotly or Folium

🧰 Tech Stack

    Python – data ingestion, ETL, analysis

    PostgreSQL – data storage and querying

    Pandas / SQLAlchemy – data manipulation

    OpenSky API – real-time flight data source

    Streamlit / Matplotlib – data visualization

    Docker (optional) – containerized environment

🗃️ Database Schema

airports (
    id SERIAL PRIMARY KEY,
    iata_code VARCHAR,
    name TEXT,
    lat FLOAT,
    lon FLOAT
)

flights (
    id SERIAL PRIMARY KEY,
    flight_number VARCHAR,
    origin_airport VARCHAR,
    destination_airport VARCHAR,
    timestamp TIMESTAMP,
    altitude INTEGER,
    status VARCHAR
)

📈 Sample Analysis

    Peak hourly traffic for JFK Airport (Past 24 hours)

SELECT DATE_TRUNC('hour', timestamp) AS hour, COUNT(*) AS flights
FROM flights
WHERE origin_airport = 'JFK'
GROUP BY hour
ORDER BY hour DESC;

🛠️ Setup Instructions

    Clone the repo

git clone https://github.com/your-username/flight-activity-tracker.git
cd flight-activity-tracker

Install requirements

pip install -r requirements.txt

Set up PostgreSQL database

createdb flight_tracker
psql flight_tracker < schema.sql

Run ETL pipeline

python etl/fetch_flight_data.py



🧠 Lessons Learned

    Built end-to-end data ingestion and storage pipeline

    Worked with time-series and geospatial data

    Applied SQL for real-time analytics

    Integrated API data with custom dashboards

📂 Project Structure

.
├── etl/
│   └── fetch_flight_data.py
├── dashboard/
│   └── app.py
├── data/
│   └── sample_data.csv
├── schema.sql
├── requirements.txt
└── README.md
# aviodata_postgres_prefect
