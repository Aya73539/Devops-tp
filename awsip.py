import urllib.request
import json
import ipaddress
import sys

def download_aws_ip_set():
    ...  # inchangé

def find_aws_ip(aws_ip_range_data, ip_to_find):
    ...  # inchangé (version avec first_ip, last_ip, num_ips)

# ---- Sous-feature 1 (branche feature/parse-ips) ----
def parse_ips(raw):
    """Transforme 'ip1,ip2,ip3' en liste d'objets ip_address."""
    return [ipaddress.ip_address(i.strip()) for i in raw.split(",")]

# ---- Sous-feature 2 (branche feature/smallest-subnet) ----
def smallest_subnet(ips):
    """Plus petit réseau contenant toutes les IPs données."""
    lo, hi = min(ips), max(ips)
    diff = int(lo) ^ int(hi)
    prefix = lo.max_prefixlen - diff.bit_length()
    return ipaddress.ip_network(f"{lo}/{prefix}", strict=False)

# ---- Sous-feature 3 (branche feature/cli-subnet) : remplace l'ancienne dernière ligne ----
if __name__ == "__main__":
    if sys.argv[1] == "subnet":
        ips = parse_ips(sys.argv[2])
        sys.stdout.write(str(smallest_subnet(ips)) + "\n")
    else:
        if __name__ == "__main__":
            if sys.argv[1] == "subnet":
                ips = parse_ips(sys.argv[2])
                sys.stdout.write(str(smallest_subnet(ips)) + "\n")
            else:
                sys.stdout.write(json.dumps(find_aws_ip(download_aws_ip_set(), sys.argv[1]), indent=2))