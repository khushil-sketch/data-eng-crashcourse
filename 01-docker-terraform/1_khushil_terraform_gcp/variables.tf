variable "credentials" {
  description = "My Credentials"
  default     = "./keys/credentials.json"
  
  #ex: if you have a directory where this file is called keys with your service account json file
  #saved there as my-creds.json you could use default = "./keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "our-velocity-468219-j5"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default     = "us-central1"
}

variable "location" {
  description = "The location for the GCS bucket"
  default     = "US"
}


variable "bq_dataset_meow" {
  description = "The name of the BigQuery dataset"
  default     = "bq_dataset_meow"
}

variable "gcp_bucket_name_meow" {
  description = "The name of the BigQuery bucket"
  default     = "gcp_bucket_name_moew"
}

variable "gcs_storage_class" {
  description = "The storage class for the GCP bucket"
  default     = "STANDARD"
}


# "our-velocity-468219-j5"