terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.47.0"
    }
  }
}

provider "google" {
  project     = var.project
  region      = var.region
  credentials = file(var.credentials) # file function is used to read the content of the file

}

resource "google_storage_bucket" "bucket_name_moew" {
  name          = var.gcp_bucket_name_meow
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }

}

resource "google_bigquery_dataset" "dataset_moew" {
  dataset_id = var.bq_dataset_meow
  location = var.location
  
}