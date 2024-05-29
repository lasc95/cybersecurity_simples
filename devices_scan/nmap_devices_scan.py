import subprocess

def scan_devices():
    nmap_output = subprocess.check_output(['nmap', '-sn', '192.168.1.0/'])

