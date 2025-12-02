import requests
from math import radians,sin,cos,sqrt,atan2
def get_location(ip):
    try:
        url=f"http://ip-api.com/json/{ip}"
        response=requests.get(url).json()
        if response["status"]=="success":
            return{
            "ip":ip,
            "city":response["city"],
            "country":response["country"],
            "lat":response["lat"],
            "lon":response["lon"]
        }
        else:
            print(f"Error finding location for {ip}")
            return None
    except Exception as e:
      print(f"An error occurred:{e}")
      return None
def calculate_distance(lat1,lon1,lat2,lon2):
    R=6371.0
    lat1,lon1,lat2,lon2=map(radians,[lat1,lon1,lat2,lon2])
    dlat=lat2-lat1
    dlon=lon2-lon1
    a=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c=2*atan2(sqrt(a),sqrt(1-a))
    distance=R*c
    return distance

if __name__=="__main__":
    ip1=input("Enter first IP address:")
    ip2=input("Enter another IP address:")
    loc1=get_location(ip1)
    loc2=get_location(ip2)
    if loc1 and loc2:
        print(f"IP address:{ip1}\nCity:{loc1['city']}\nCountry:{loc1['country']}\nLat:{loc1['lat']}\nLon:{loc1['lon']}\n")
        print(f"IP address:{ip2}\nCity:{loc2['city']}\nCountry:{loc2['country']}\nLat:{loc2['lat']}\nLon:{loc2['lon']}\n")
        distance=calculate_distance(loc1['lat'],loc1['lon'],loc2['lat'],loc2['lon'])
        print(f"Approximate distance between the IP addresses are:{distance:.2f} kms")
