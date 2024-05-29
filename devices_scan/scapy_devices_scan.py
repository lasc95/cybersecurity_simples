import scapy

def scan_devices():
    # definimos la dirección ip de mi red
    network_ip = '192.168.1.1'

    # creamos un paquete DHCP para la solicitud
    dhcp_request = scapy.DHCP(op=1, hwid=scapy.RandMAC())

    # enviamos la solicitud y capturamos las respuestas
    responses = scapy.sr(dhcp_request, dst=network_ip, timeout=10)

    # extraemos las direcciones MAC e IP de las respuestas
    devices = []

    for response in responses:
        if response.answered:
            ip = response[scapy.DHCP].yiaddr
            mac = response[scapy.DHCP].chaddr.hwaddr
            devices.append((ip, mac))
    
    print('Dispositivos encontrados')
    for ip, mac in devices:
        print(f'ip: {ip} - MAC {mac}')

if __name__ == '__main__':
    scan_devices()
