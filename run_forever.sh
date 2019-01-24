#!/bin/bash

set -euo pipefail

while true
do
  python gcloud_dns_updater.py
  sleep "$INTERVAL"
done
