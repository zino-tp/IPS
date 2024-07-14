import os
import requests
import socket

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_public_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return str(e)

def ip_lookup(ip_address):
    clear_screen()
    print("==============================")
    print("        IP Address Lookup")
    print("==============================")

    print(f"Looking up information for IP address {ip_address}...")

    # Check if IPv4 or IPv6
    if ':' in ip_address:
        # IPv6 lookup using ip-api.com
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
    else:
        # IPv4 lookup using ipinfo.io
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")

    if response.status_code == 200:
        data = response.json()
        print("\nIP Address Information:")
        print("==============================")
        print(f"IP Address: {data.get('ip')}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print("==============================")
    else:
        print(f"Fehler beim Abrufen der Informationen für IP-Adresse {ip_address}.")
    
    input("Press Enter to continue...")

def show_network_info():
    clear_screen()
    print("==============================")
    print("       Network Information")
    print("==============================")

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f"Hostname: {hostname}")
    print(f"Local IP Address: {local_ip}")

    try:
        public_ip = get_public_ip()
        print(f"Public IP Address: {public_ip}")
    except Exception as e:
        print(f"Failed to retrieve public IP address: {e}")

    input("Press Enter to continue...")

if __name__ == "__main__":
    while True:
        clear_screen()
        print("Wählen Sie aus:")
        print("1. IP Address Lookup (IPv4)")
        print("2. IP Address Lookup (IPv6)")
        print("3. My Infos")
        print("4. Beenden")
        choice = input("Ihre Auswahl (1/2/3/4): ")

        if choice == "1":
            ip_address = input("Geben Sie eine IPv4 Adresse ein: ")
            ip_lookup(ip_address)
        elif choice == "2":
            ip_address = input("Geben Sie eine IPv6 Adresse ein: ")
            ip_lookup(ip_address)
        elif choice == "3":
            show_network_info()
        elif choice == "4":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie erneut.")
            input("Press Enter to continue...")
