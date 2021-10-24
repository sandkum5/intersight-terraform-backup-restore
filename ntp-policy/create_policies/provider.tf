terraform {
  required_providers {
    intersight = {
      source = "CiscoDevNet/intersight"
      # version = "1.0.16"
    }
  }
}

provider "intersight" {
  apikey        = "Enter_the_API_KEY"
  secretkey     = "SecretKey.txt"
  endpoint      = "https://intersight.com"
}
