"""

"""

import subprocess

def scan_networks():
    # Ejecutamos el comando nmap para escanear la red
    nmap_output = subprocess.check_output(["nmap", "-A", "-sn", "192.168.1.0/24"])

    # procesa la salida de nmap y extraemos las direcciones ip
    ip_addresses = []
    for line in nmap_output.decode().split("\n"):
        if line.starwith('192.168'):
            ip_addresses.append(line.split()[0])

    # imprime las direcciones IP detectadas
    print('Redes detectadas: ')
    for ip in ip_addresses:
        print(ip)

if __name__ == '__main__':
    scan_networks()
