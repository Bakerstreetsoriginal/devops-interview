import requests
from datetime import datetime, timezone

# variables
lat = 50.930581
lon = 5.780691
format = 0
api_url = "https://api.sunrise-sunset.org/json?lat=%f&lon=%f&formatted=%s" % (
    lat, lon, format)


def lights():
    # Do the api request and save the response to a json compatible variable
    getSunTimes = requests.get(api_url)
    sunTimes = getSunTimes.json()

    # extract the values from the json and make sure they are of the same format
    sunSetTime = sunTimes["results"]["sunset"].format().replace("+00:00", "Z")
    sunRiseTime = sunTimes["results"]["sunrise"].format().replace(
        "+00:00", "Z")
    currentTime = datetime.utcnow().isoformat(
    )[:-3]+'Z'.format().replace("+00:00", "Z")

    # for debugging
    # print(sunSetTime)
    # print(sunRiseTime)
    # print(currentTime)

    # conditional statements to define if the lights should be on or off
    if (sunSetTime < currentTime) or (sunRiseTime > currentTime):
        print("ON")
    else:
        print("OFF")


lights()