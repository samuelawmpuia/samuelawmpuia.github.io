import requests

x = requests.get("https://www.affirmations.dev/")
print(x.json())

