"""
scapy es una biblioteca de bajo nivel que permite enviar y recibir paquetes de red, otorga un control granular
sobre el proceso de escaneo
"""
import scapy.all as scapy

def scan_networks():
    # Define the IP range to scan
    ip_range = "192.168.1.0/24"

    # Create and send ARP request packets
    arp_request = scapy.ARP(pdst=ip_range)
    responses = scapy.srp(arp_request, timeout=10)

    # Extract information only from ARP responses
    devices = []
    for response in responses[0]:  # Iterate through received packets list
        if scapy.ARP in response:  # Check if it's an ARP response
            ip = response[scapy.ARP].psrc
            mac = response[scapy.ARP].hwsrc
            devices.append((ip, mac))

    # Print information about detected devices
    print("Detected devices:")
    for ip, mac in devices:
        print(f"IP: {ip}, MAC: {mac}")

if __name__ == "__main__":
    scan_networks()

