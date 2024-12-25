from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from .models import Location, WeatherData

def get_weather_data(location_name):
    api_key = 'YOUR_API_KEY'  # Get your API key from OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def weather_view(request):
    if request.method == 'POST':
        location_name = request.POST.get('location')
        weather_data = get_weather_data(location_name)
        
        if weather_data.get('main'):
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            condition = weather_data['weather'][0]['description']
            location = Location.objects.get_or_create(name=location_name)[0]
            WeatherData.objects.create(location=location, temperature=temperature, humidity=humidity, condition=condition)
            context = {
                'location': location_name,
                'temperature': temperature,
                'humidity': humidity,
                'condition': condition,
            }
            return render(request, 'weather/weather.html', context)
    
    return render(request, 'weather/weather.html')
