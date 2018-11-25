gcloud_dns_updater
===============

Python script to be ran inside a Kubernetes cluster to grab nodes' IPs and update corresponding DNS records in a Google Cloud Domain.

Configuration
-------------

This script expects the following env vars to be set:

- `GCLOUD_ZONE_NAME`, `GCLOUD_DOMAIN`:

Details of the Google Cloud Managed Zone to update. For example, `GCLOUD_ZONE_NAME=acme-co` and `GCLOUD_DOMAIN=example.com`

- `DNS_ZONE`, `DNS_SUBDOMAIN`:

Zone and subdomain, e.g. `DNS_ZONE=example.dom` `DNS_SUBDOMAIN=kubernetes` to update DNS records for [kubernetes.example.com](kubernetes.example.com)

Run
---

    python ./gcloud_dns_updater.py
