# aviodata_postgres_prefect

**Aviation Data Pipeline with Prefect, PostgreSQL, and OpenSky API**

This repository implements a robust data ingestion and processing pipeline to fetch aviation data via the OpenSky API, store it in PostgreSQL, and orchestrate workflows using Prefect.

---

##  Overview

- **Fetch real-time or historical flight data** using the OpenSky API.
- **Store and manage data** in PostgreSQL using `psycopg2` or `SQLAlchemy`.
- **Pipeline orchestration** through Prefect for scheduling, monitoring, and retries.
- **Core modules** for data ingestion, geolocation, database operations, and main workflow orchestration.

---

##  File Structure

.
├── get_location.py # Utilities for determining location data
├── ingest_data.py # Functions to fetch and prepare flight data
├── openSky_api.py # Handles communication with the OpenSky API
├── postgres_functions.py # Database connection, schema creation, and data insertion
├── main.py # Orchestrates the Prefect workflow
├── requirements.txt # Python dependencies
└── README.md # Project overview and instructions


---

##  Technical Stack

- **Python** – Core scripting and orchestration
- **Prefect** – Workflow management and scheduling
- **PostgreSQL** – Relational database for storing and querying flight data
- **OpenSky API** – Source of aviation data
- **psycopg2** / **SQLAlchemy** – Database interaction and ORM support
- **(Optional)** Geospatial libraries for enrichments (e.g., Shapely, GeoPandas)

---

### Prerequisites

- Python 3.8+
- PostgreSQL server accessible and configured
- API credentials (if required by OpenSky or proxy setup)

**Clone the repository**

   ```bash
   git clone https://github.com/konstantina54/aviodata_postgres_prefect.git
   cd aviodata_postgres_prefect

    Install dependencies

pip install -r requirements.txt

Prepare the PostgreSQL database

CREATE DATABASE aviodata;
-- Then in your terminal:
psql -d aviodata -f path/to/schema.sql  # If a schema file exists

Configure environment variables (if used)

export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=aviodata
export DB_USER=your_username
export DB_PASSWORD=your_password

Test API connectivity

python openSky_api.py

Run data ingestion

python ingest_data.py

Initialize the Prefect workflow

Visualize and run via Prefect:

prefect orion start
prefect deployments build main.py:flow --name="flight-data-pipeline"
prefect deployment apply flight-data-pipeline-deployment.yaml
prefect deployment run flight-data-pipeline
