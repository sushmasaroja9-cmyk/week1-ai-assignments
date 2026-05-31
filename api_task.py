import requests

# Fetch data from Cat Facts API
url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("=== CAT FACT ===")
    print("Fact:", data["fact"])
    print("Length:", data["length"])

else:
    print("Failed to fetch data.")
