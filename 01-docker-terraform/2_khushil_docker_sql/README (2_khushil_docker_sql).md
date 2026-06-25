# NYC Taxi Data Engineering Pipeline

An end-to-end data ingestion pipeline that loads 1M+ NYC yellow taxi trip records into a PostgreSQL database, containerized with Docker and provisioned on Google Cloud Platform.

## What This Does

- Ingests NYC TLC yellow taxi trip data (January 2021) from a raw CSV/Parquet source into a PostgreSQL database
- Containerizes the ingestion script and Postgres instance using Docker and Docker Compose
- Connects pgAdmin as a query and validation interface within the same Docker network
- Runs SQL analysis across the ingested dataset — joins, aggregations, NULL checks, and data quality validation

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python (pandas) | Data ingestion and transformation script |
| PostgreSQL | Target database |
| Docker + Docker Compose | Container orchestration |
| pgAdmin | Query interface and data validation |
| GCP Cloud VM | Cloud deployment environment |
| Terraform | Infrastructure provisioning |
| Git | Version control |

## Project Structure

```
├── pandas_ingest.py          # Parameterized ingestion script (argparse)
├── Dockerfile.pandas_ingest  # Dockerized ingestion script
├── Dockerfile.simple         # Simplified Docker image
├── khushil_docker_compose.yml # Multi-container orchestration (Postgres + pgAdmin)
├── pipeline.py               # Standalone pipeline script
├── pandas_notebook.ipynb     # Exploratory querying and validation notebook
├── output.parquet            # Sample output in Parquet format
├── setting_up_postgres_image.txt  # Setup notes
├── running_pandas_ingest.txt      # Run instructions
└── data_dictionary_trip_records_yellow.pdf  # Dataset schema reference
```

## How to Run

### 1. Start Postgres and pgAdmin with Docker Compose

```bash
docker-compose -f khushil_docker_compose.yml up
```

This spins up two containers on a shared network:
- PostgreSQL on port `5432`
- pgAdmin on port `8080` → accessible at `http://localhost:8080`

### 2. Run the ingestion script

```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

python pandas_ingest.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=${URL}
```

### 3. Or run it fully containerized

```bash
docker build -f Dockerfile.pandas_ingest -t taxi_ingest:v001 .

docker run -it --network=pg-network taxi_ingest:v001 \
  --user=root --password=root \
  --host=pg-database --port=5432 \
  --db=ny_taxi --table_name=yellow_taxi_trips \
  --url=${URL}
```

## SQL Analysis

Queries in `pandas_notebook.ipynb` cover:

- **INNER, LEFT, RIGHT, OUTER JOINs** — joining trip data with taxi zone lookup table
- **NULL checks** — identifying records with missing pickup/dropoff location IDs
- **GROUP BY + aggregations** — trip counts, max fares, passenger counts by day
- **Data quality validation** — checking for location IDs not present in the zones table

## Cloud Deployment

The pipeline was deployed on a **GCP Cloud VM**, with infrastructure provisioned using **Terraform**. The full analytics stack (Docker, Python, pgcli, Docker Compose) was configured via SSH on the remote instance.

---

Built as part of the [DataTalksClub Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp).
