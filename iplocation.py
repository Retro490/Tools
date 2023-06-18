import geocoder

def geolocate_ip(ip_address):
    g = geocoder.ip(ip_address)
    
    if g.ok:
        return g.json

    return None

# Esegui la funzione principale
if __name__ == "__main__":
    ip_address = input("Inserisci l'indirizzo IP da localizzare: ")
    location = geolocate_ip(ip_address)
    
    if location:
        print("Dettagli di localizzazione per l'IP {}: ".format(ip_address))
        print("Paese: ", location.get("country"))
        print("Città: ", location.get("city"))
        print("Regione: ", location.get("region"))
        print("Coordinate: ", location.get("lat"), ",", location.get("lng"))
    else:
        print("Impossibile localizzare l'IP: ", ip_address)
