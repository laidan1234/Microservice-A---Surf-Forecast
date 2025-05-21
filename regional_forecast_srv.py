import random

file = "regional_forecast_service.txt"
forecasts = [[75, 64, 2.3, 5], [57, 50, 5.6, 8]]

while True:
    pipe = open(file, "r+")
    region = pipe.readline()
    if region != "":
        continue
    else:
        forecast = forecasts[random.randint(0, len(forecasts) - 1)]
        pipe.seek(0)
        pipe.write(f"Air temperature: {str(forecast[0])}, Water Temperature: {str(forecast[1])}"
        f", Average Wave Height: {forecast[2]}, Windspeed: {str(forecast[3])}")
        pipe.truncate()
    pipe.close()

