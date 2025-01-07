import requests


ort = input("gib ein Ort ein: ")
respense = requests.get(f"http://wttr.in/{ort}?format=j1")
daten = respense.json()
# print(daten)
current_condition = daten.get("current_condition", [])[0]


area_name = daten["nearest_area"][0]["areaName"]
print(f"  Area name: {area_name}")

temperatur = daten["current_condition"][0]["temp_C"]
print(f"  Temperatur: {temperatur}°C")

gefuhl_temperatur = daten["current_condition"][0]["FeelsLikeC"]
print(f"  Gefühlte Temperatur: {gefuhl_temperatur}°C")
