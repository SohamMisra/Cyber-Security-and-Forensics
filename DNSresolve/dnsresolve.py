import socket
import requests
def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror as e:
        print(f"Error obtaining address for {domain}:{e}")
        return None
def get_location(ip):
    try:
        url=f"https://ipinfo.io/{ip}/json"
        response=requests.get(url,timeout=5)
        data=response.json()
        return{
            "ip":data.get("ip"),
            "city":data.get("city"),
            "region":data.get("region"),
            "country":data.get("country"),
            "org":data.get("org")
        }
    except Exception as e:
        print(f"An unexpected error occurred:{e}")
        return None
domain=input('Enter a domain name(e.g. www.google.com):')
ip=get_ip(domain)
if ip:
    print(f"\nThe IP address for {domain}:{ip}")
    location=get_location(ip)
    if location:
        print('Location info:')
        for k,v in location.items():
         print(f" {k}:{v}")
