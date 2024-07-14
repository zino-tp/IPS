import socket
import requests

def get_ip_info(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()
        if data['status'] == 'success':
            return data
        else:
            return None
    except Exception as e:
        print(f"Error retrieving IP information: {e}")
        return None

def display_ip_info(data):
    print("\n--- IP Information ---")
    print(f"IP Address: {data.get('query')}")
    print(f"City: {data.get('city')}")
    print(f"Region: {data.get('regionName')}")
    print(f"Country: {data.get('country')}")
    print(f"ISP: {data.get('isp')}")
    print(f"Organization: {data.get('org')}")
    print(f"AS: {data.get('as')}")
    print(f"Postal Code: {data.get('zip')}")
    print(f"Time Zone: {data.get('timezone')}")
    print(f"Coordinates: {data.get('lat')}, {data.get('lon')}")
    print("----------------------")

def get_local_ip_address(ip_type):
    if ip_type == 'IPv4':
        return socket.gethostbyname(socket.gethostname())
    elif ip_type == 'IPv6':
        return socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]

def display_my_info():
    ipv4 = get_local_ip_address('IPv4')
    ipv6 = get_local_ip_address('IPv6')
    wlan_ipv4 = ipv4  # Assuming WLAN IPv4 is the same as the local IPv4
    wlan_ipv6 = ipv6  # Assuming WLAN IPv6 is the same as the local IPv6
    
    print("\n--- My Information ---")
    print(f"IPv4: {ipv4}")
    print(f"IPv6: {ipv6}")
    print(f"WLAN IPv4: {wlan_ipv4}")
    print(f"WLAN IPv6: {wlan_ipv6}")
    print("----------------------")

def main():
    print("Welcome to Z-Tracker")
    print("====================")
    print("Select the type of IP you want to track:")
    print("1. IPv4")
    print("2. IPv6")
    print("3. WLAN IP Address (IPv4)")
    print("4. WLAN IP Address (IPv6)")
    print("5. Regular IP Address")
    print("6. My Information")
    print("====================")
    
    choice = input("Enter the number of the IP type: ")

    ip_type_dict = {
        '1': 'IPv4',
        '2': 'IPv6',
        '3': 'WLAN IPv4',
        '4': 'WLAN IPv6',
        '5': 'Regular IP Address'
    }

    if choice == '6':
        display_my_info()
    elif choice in ip_type_dict:
        ip_type = ip_type_dict[choice]

        if choice in ['3', '4']:
            ip_address = get_local_ip_address(ip_type.split()[1])
            print(f"Your current {ip_type} is: {ip_address}")
        else:
            ip_address = input(f"Enter the {ip_type} you want to track: ")

        ip_info = get_ip_info(ip_address)
        if ip_info:
            display_ip_info(ip_info)
        else:
            print("Could not retrieve information for the IP address.")
    else:
        print("Invalid selection. Please restart the program and choose a valid option.")

if __name__ == "__main__":
    main()
