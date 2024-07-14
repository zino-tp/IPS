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
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
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
            print("IPv6 Lookup wird nicht unterstützt.")
            input("Press Enter to continue...")
        elif choice == "3":
            show_network_info()
        elif choice == "4":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie erneut.")
            input("Press Enter to continue...")
