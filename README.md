# Microservice A - Surf Regional Forecast
This microservice responds to an input region given by the user and returns a surf forecast for that region. 
The information returned inlucdes air temperature, water temperature, average wave height, and windspeed 
all communicated via text file.

## How to make a request
This microservice responds written changes to a text file by the calling program. 
### Example call from calling program
```
user_input = input("Enter a region: ")
        if user_input != "":
            regional_forecast_pipe = open(file_regional_forecast_srv, "w+")
            regional_forecast_pipe.write(user_input)
            regional_forecast_pipe.close()
```
The above call takes a region as user input and writes the region to the text file. 

## How to receive the forecast
As mentioned earlier,the microservice communicates its return values via the same text file the request was written to.
### Example call from calling program
```
regional_forecast_pipe = open(file_regional_forecast_srv, "r")
forecast = regional_forecast_pipe.readline()
regional_forecast_pipe.close()
```
The above call opens the text and reads the microservice's output from it.
