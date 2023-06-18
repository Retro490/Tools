import socket

def scan_network():
    devices = []
    ip_prefix = '.'.join(socket.gethostbyname(socket.gethostname()).split('.')[:-1]) + '.'

    for i in range(1, 255):
        ip_address = ip_prefix + str(i)
        try:
            host_name = socket.gethostbyaddr(ip_address)[0]
            devices.append({'ip': ip_address, 'hostname': host_name})
        except socket.herror:
            pass

    return devices

def print_devices(devices):
    print("Dispositivi connessi in rete:")
    print("IP\t\t\tHostname")
    print("-----------------------------------------")
    for device in devices:
        print(device['ip'] + "\t" + device['hostname'])

# Esegui la funzione principale
if __name__ == "__main__":
    devices = scan_network()
    print_devices(devices)
