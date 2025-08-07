terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.47.0"
    }
  }
}

provider "google" {
  project = "our-velocity-468219-j5"
  region  = "us-central1"
}