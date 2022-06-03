from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import phonenumbers
import opencage
import folium
from number import number

from phonenumbers import geocoder

ch_number = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_number, "en")
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


key = 'OPENCAGE KEY HERE'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("location.html")
