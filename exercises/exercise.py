travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Access the "5" in the second dictionary
countries = []
for visit in travel_log:
    countries.append(travel_log[1]["country"])

print(countries) 
