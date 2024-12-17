# recon_modules/dns_lookup.py
def dns_lookup(domain):
    import socket

    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] {domain} resolved to {ip}")
    except socket.gaierror:
        print("[!] Failed to resolve domain. Check if the domain is correct.")
