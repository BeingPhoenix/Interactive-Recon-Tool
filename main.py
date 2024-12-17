# main.py
import os
import socket
import threading
import time
from recon_modules.port_scanner import port_scanner
from recon_modules.dns_lookup import dns_lookup

def display_banner():
    """ Display a banner when the tool starts. """
    banner_path = "assets/banner.txt"
    if os.path.exists(banner_path):
        with open(banner_path, "r") as banner_file:
            banner = banner_file.read()
            print(banner)
    else:
        print("\n[!] Banner file missing. Welcome to the Interactive Recon Tool!\n")

def main_menu():
    """ Display the main menu options. """
    print("\n======================== Main Menu ========================")
    print("[1] Port Scanning")
    print("[2] DNS Lookup")
    print("[3] Advanced Options")
    print("[4] Exit")
    print("==========================================================\n")
    choice = input("Enter your choice: ").strip()
    return choice

def validate_ip(ip):
    """ Validate the given IP address. """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def validate_port_range(start_port, end_port):
    """ Validate the given port range. """
    return 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port

def advanced_options():
    """ Display additional advanced options for future modules. """
    print("\n========= Advanced Options =========\n")
    print("[1] About Tool")
    print("[2] View Documentation")
    print("[3] Go Back to Main Menu\n")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        print("\nInteractive Recon Tool - Version 1.0")
        print("Developed for Kali Linux using Python.")
        print("Modules: Port Scanning, DNS Lookup.")
    elif choice == "2":
        print("\n[+] Documentation can be found at: /docs/interactive_recon_tool.md")
    elif choice == "3":
        print("\n[+] Returning to Main Menu...")
    else:
        print("\n[!] Invalid choice in Advanced Options.")

def main():
    """ The main loop of the tool. """
    os.system("clear")  # Clear the terminal for better visuals
    display_banner()
    while True:
        choice = main_menu()
        if choice == "1":
            print("\n========= Port Scanner =========\n")
            target = input("Enter the target IP address: ").strip()
            if not validate_ip(target):
                print("[!] Invalid IP address. Please try again.")
                continue
            try:
                start_port = int(input("Enter the start port (default 1): ") or 1)
                end_port = int(input("Enter the end port (default 1024): ") or 1024)
                if not validate_port_range(start_port, end_port):
                    print("[!] Invalid port range. Ports must be between 1 and 65535.")
                    continue
                threads = int(input("Enter the number of threads (default 10): ") or 10)
                print("\n[+] Starting Port Scan...\n")
                start_time = time.time()
                port_scanner(target, start_port, end_port, threads)
                print(f"\n[+] Port Scan Completed in {time.time() - start_time:.2f} seconds")
            except ValueError:
                print("[!] Invalid input. Please enter valid numbers.")
        elif choice == "2":
            print("\n========= DNS Lookup =========\n")
            domain = input("Enter the domain to lookup: ").strip()
            if not domain:
                print("[!] Domain cannot be empty. Please try again.")
                continue
            print("\n[+] Performing DNS Lookup...\n")
            try:
                dns_lookup(domain)
            except Exception as e:
                print(f"[!] DNS Lookup Failed: {e}")
        elif choice == "3":
            advanced_options()
        elif choice == "4":
            print("\n[+] Exiting... Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()

