import requests
from twilio.rest import Client

API_KEY = "534c7eda483e6b5979a6bdf52d1bcfac"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC2a27ebe78622aca249dd386b6e9b3560"
auth_token = "0ff11a32a7f841cc60fba6f149ad8041"


LAT = 51.507351
LONG = -0.127758

weather_params ={
   "lat":LAT,
    "lon":LONG,
    "appid": API_KEY,
     "cnt":3,
}

# responce = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&appid={API_KEY}")
responce = requests.get(OWM_Endpoint,params = weather_params)
responce.raise_for_status()

weather_data = responce.json()
weather_id = weather_data["list"][0]["weather"][0]["id"]
days=weather_data["list"][0]

for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id)<700:
        will_rain =True

if will_rain:
    print("Bring an Umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hi Hi. It's going to rain today. Brign an umbrella",
        from_='+447481345031',
        to='[Verified Mobile Number]'
    )

    print(message.status)