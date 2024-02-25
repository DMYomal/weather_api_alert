import requests
API_KEY = "534c7eda483e6b5979a6bdf52d1bcfac"

LAT = 51.507351
LONG = -0.127758

responce = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&appid={API_KEY}")
status_code = responce.raise_for_status()

data = responce.json()
print(status_code)
print(data)
# https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=534c7eda483e6b5979a6bdf52d1bcfac