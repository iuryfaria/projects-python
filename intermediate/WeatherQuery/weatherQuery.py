# Import the requests library
# It is used to make HTTP requests (GET, POST, etc.)
import requests

# Your OpenWeatherMap API key
# This key identifies your application to the API
API_KEY = 'your_api_key' 
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = input("Enter city name: ")

# Base URL of the current weather API
url = (f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric")

# Send an HTTP GET request to the API
response = requests.get(url)

# Check if the request was successful
# Status code 200 means OK
if response.status_code == 200:
    # Convert the API response from JSON to a Python dictionary
    data = response.json()

    # Get the temperature from the response
    # 'main' contains temperature-related data
    temp = data['main']['temp']
    
    # Get the weather description
    # 'weather' is a list, so we access the first element
    weather_desc = data['weather'][0]['description']

    print(f"Temperature in {city}: {temp}°C")
    print(f"Weather: {weather_desc}")

else:
    # This block runs if the API returns an error
    # Common errors: 401 (invalid API key), 404 (city not found)
    print("Error fetching weather data or error API. Please check the city name and try again.")