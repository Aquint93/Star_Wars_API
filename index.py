import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data = []
  try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(f"Successfully fetched {len(data)} entities")
  except requests.HTTPError as e:
    print(f"Error retrieving data due to {e}")
    return None

  return data
 

data = fetch_data("people")
if data:
  for element in data:
    print(element["name"])
else:
  print("Unable to download data")