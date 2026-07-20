# Cloud Infrastructure Provisioning (Terraform & GCP)

## Objective
This module contains the Infrastructure as Code (IaC) configuration required to set up the foundational cloud environment for the NYC Taxi Data Engineering pipeline. 

Instead of manually provisioning resources via the Google Cloud Console, Terraform is used to automate the deployment of a scalable data lake and data warehouse environment. This ensures the infrastructure is reproducible, version-controlled, and easily teardown-able.

## Tech Stack
* **Infrastructure as Code:** Terraform
* **Cloud Provider:** Google Cloud Platform (GCP)
* **Data Lake:** Google Cloud Storage (GCS)
* **Data Warehouse:** Google BigQuery

## What This Code Does
Running the Terraform scripts in this directory automatically provisions two core GCP resources:
1. **GCS Bucket:** Acts as the Data Lake to store the raw, parquet-formatted NYC Taxi trip records.
2. **BigQuery Dataset:** Acts as the Data Warehouse where the raw data will eventually be modeled and queried for analytics.

## Execution Steps
To replicate this infrastructure setup locally:

1. Ensure you have the [Terraform CLI](https://developer.hashicorp.com/terraform/downloads) installed and a GCP account with billing enabled.
2. Authenticate your Google Cloud environment using your service account credentials:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-keys>.json"
