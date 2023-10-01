travel_log = {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    }

countries = []
for visit in travel_log:
    countries.append(travel_log[1]["country"])

print(countries) 
