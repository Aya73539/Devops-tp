import urllib.request
import json
import ipaddress
import sys

def find_aws_ip(aws_ip_range_data, ip_to_find):
    """Finds the AWS IP range that contains the given IP address."""
    ip = ipaddress.ip_address(ip_to_find)
    results = []
    for prefix in aws_ip_range_data:
        network = ipaddress.ip_network(prefix['ip_prefix'])
        if ip in network:
            results.append({**prefix,
                            'first_ip': str(network[0]),
                            'last_ip': str(network[-1]),
                            'num_ips': network.num_addresses})
    return results

def parse_ips(raw):
    """Transforme 'ip1,ip2,ip3' en liste d'objets ip_address."""
    return [ipaddress.ip_address(i.strip()) for i in raw.split(",")]