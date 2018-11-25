import json
import os
from google.cloud import dns
from kubernetes import client, config

# Sanity checks
for k in [
        'GCLOUD_ZONE_NAME',
        'GCLOUD_DOMAIN',
        'DNS_ZONE',
        'DNS_SUBDOMAIN',
        ]:
    if k not in os.environ:
        raise KeyError('Required env var ' + k + ' not found in environment!')

# Config mapping
zone      = os.getenv('DNS_ZONE')
subdomain = os.getenv('DNS_SUBDOMAIN')
ttl       = os.getenv('DNS_TTL', 30)

# Configs can be set in Configuration class directly or using helper utility
config.load_incluster_config()

v1 = client.CoreV1Api()
ret = v1.list_node(watch=False)
external_ips = []
for node in ret.items:
    external_ips += [i.address
            for i in node.status.addresses
            if i.type == 'ExternalIP']

print("Current node ExternalIPs: %s" % external_ips)

client    = dns.Client()
zone_name = os.getenv('GCLOUD_ZONE_NAME')
domain    = os.getenv('GCLOUD_DOMAIN')

zone = client.zone(zone_name, domain)
record_set = zone.resource_record_set(
   'www.example.com.',
   'A',
   30,
   external_ips)
changes = zone.changes()
changes.add_record_set(record_set)
changes.create()
while changes.status != 'done':
    print('Waiting for changes to complete...')
    time.sleep(10)
    changes.reload()
