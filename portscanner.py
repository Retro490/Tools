import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Imposta il timeout a 1 secondo
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"La porta {port} è aperta")
        else:
            print(f"La porta {port} è chiusa")
        sock.close()
    except socket.error:
        print("Errore durante la connessione al server")

def scan_ip(ip):
    print(f"Scansione delle porte aperte per l'indirizzo IP: {ip}")
    ports = [21, 22, 80, 443]  # Elenca le porte che desideri scansionare

    for port in ports:
        scan_port(ip, port)

ip_address = input("Inserisci l'indirizzo IP da scansionare: ")
scan_ip(ip_address)
