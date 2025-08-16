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