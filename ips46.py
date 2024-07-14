import tkinter as tk
from tkinter import messagebox
import requests
from ipwhois import IPWhois

# Funktion zum Abrufen von IP-Informationen
def get_ip_info(ip):
    try:
        obj = IPWhois(ip)
        details = obj.lookup_rdap()
        return details
    except Exception as e:
        return str(e)

# Funktion zum Abrufen der Standortinformationen
def get_location_info(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        return response.json()
    except Exception as e:
        return str(e)

# Funktion, um die eigene öffentliche IP-Adresse zu erhalten
def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip')
    except Exception as e:
        return str(e)

# Funktion, die ausgeführt wird, wenn der Button geklickt wird
def track_ip():
    choice = selection.get()
    if choice == "My Infos":
        ip = get_public_ip()
    else:
        ip = entry.get()
    
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
        ip_details = ip_info

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

    messagebox.showinfo("IP-Informationen", f"{ip_details}\n\n{location_details}")

# Erstellen des GUI-Fensters
root = tk.Tk()
root.title("IP Tracker")

label = tk.Label(root, text="Geben Sie eine IPv4 oder IPv6 Adresse ein:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

selection = tk.StringVar(value="Enter IP")
radio1 = tk.Radiobutton(root, text="Enter IP", variable=selection, value="Enter IP")
radio1.pack(anchor=tk.W)
radio2 = tk.Radiobutton(root, text="My Infos", variable=selection, value="My Infos")
radio2.pack(anchor=tk.W)

button = tk.Button(root, text="Track IP", command=track_ip)
button.pack(pady=20)

root.mainloop()
