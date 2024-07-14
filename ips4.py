import requests
from ipwhois import IPWhois
import socket

def get_ip_info(ip):
    try:
        obj = IPWhois(ip)
        details = obj.lookup_rdap()
        return details
    except Exception as e:
        return str(e)

def get_location_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        return response.json()
    except Exception as e:
        return str(e)

def get_public_ip():
    try:
        # Automatisch die öffentliche IP-Adresse des Geräts abrufen
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return str(e)

def track_ip(ip_choice):
    if ip_choice == "Enter IP":
        ip = input("Geben Sie eine IPv4 oder IPv6 Adresse ein: ")
    elif ip_choice == "My Infos":
        ip = get_public_ip()
    else:
        print("Ungültige Auswahl.")
        return

    ip_info = get_ip_info(ip)
    location_info = get_location_info(ip)

    if isinstance(ip_info, dict):
        ip_details = f"""
        IP-Adresse: {ip}
        Netzwerk: {ip_info.get('network')}
        ASN: {ip_info.get('asn')}
        ASN-CIDR: {ip_info.get('asn_cidr')}
        ASN-Country-Code: {ip_info.get('asn_country_code')}
        ASN-Date: {ip_info.get('asn_date')}
        ASN-Registry: {ip_info.get('asn_registry')}
        """
    else:
        ip_details = f"Fehler beim Abrufen der IP-Informationen: {ip_info}"

    if isinstance(location_info, dict) and location_info.get('status') == 'success':
        location_details = f"""
        Land: {location_info.get('country')}
        Region: {location_info.get('regionName')}
        Stadt: {location_info.get('city')}
        PLZ: {location_info.get('zip')}
        Breitengrad: {location_info.get('lat')}
        Längengrad: {location_info.get('lon')}
        """
    else:
        location_details = "Keine Standortinformationen verfügbar."

    print(ip_details)
    print(location_details)

if __name__ == "__main__":
    print("Wählen Sie aus:")
    print("1. Enter IP")
    print("2. My Infos")
    choice = input("Ihre Auswahl (1/2): ")

    if choice == "1":
        track_ip("Enter IP")
    elif choice == "2":
        track_ip("My Infos")
    else:
        print("Ungültige Auswahl.")
