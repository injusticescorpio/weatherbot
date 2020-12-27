import requests
import json
class Weather:
    def weather_detail(self,city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=API KEY here"
        weather = requests.get(url).json()
        print(weather)
        return(f"Description         ->  {(weather['weather'][0]['description']).title()} \n Temperature         ->  {weather['main']['temp']} degree celsius  \n Pressure            ->  {weather['main']['pressure']} \n Humidity            ->  {weather['main']['humidity']} \n Wind speed          ->  {weather['wind']['speed']}")
        

        
