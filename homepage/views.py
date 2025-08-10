from django.shortcuts import render
import os
import requests
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'your openweather api key')

def get_weather_state(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        weather_response = "unknown"
        if 'weather' in data and len(data['weather']) > 0:
            print(f"DATA: {data}")
            # {'coord': {'lon': 101.6865, 'lat': 3.1431}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 28.49, 'feels_like': 31.33, 'temp_min': 28.49, 'temp_max': 28.49, 'pressure': 1009, 'humidity': 68, 'sea_level': 1009, 'grnd_level': 996}, 'visibility': 10000, 'wind': {'speed': 1.4, 'deg': 218, 'gust': 1.6}, 'rain': {'1h': 1}, 'clouds': {'all': 100}, 'dt': 1754810722, 'sys': {'country': 'MY', 'sunrise': 1754781104, 'sunset': 1754825140}, 'timezone': 28800, 'id': 1733046, 'name': 'Kuala Lumpur', 'cod': 200}

            main_weather = data['weather'][0]['main'].lower()
            if "cloud" in main_weather:
                weather_response = 'cloudy'
            elif "rain" in main_weather:
                weather_response = 'raining'
            elif "clear" in main_weather:
                weather_response = 'sunny'
        return weather_response

    except Exception:
        return 'unknown'

def index(request):
    location = request.GET.get('location', '').strip()
    weather = None
    if location:
        weather = get_weather_state(location)
    return render(request, 'homepage/index.html', {
        'location': location,
        'weather': weather,
    })