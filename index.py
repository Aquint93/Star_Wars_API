import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data = []
  try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    print(f"Able to access {len(data)} items of data.")
  except requests.HTTPError as e:
    print("Unable to access data")
    return None

  return data

option = input("What Star Wars data would you like to explore? ").strip().lower()
data = fetch_data(option)

if data:
  for item in data:
    print(item["name"])
else:
    print("Unable to download data")
