# Create a Virtual Environment:

# Run the following commands in the terminal:
# python -m venv venv
# source venv/bin/activate  # On Windows use `venv\Scripts\activate`

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather App</title>
</head>
<body>
    <h1>Weather in {{ city }}</h1>
    <form method="GET">
        <input type="text" name="city" placeholder="Enter city name">
        <button type="submit">Get Weather</button>
    </form>
    {% if temperature %}
        <p>Temperature: {{ temperature }}°C</p>
        <p>Description: {{ description }}</p>
        <img src="http://openweathermap.org/img/wn/{{ icon }}@2x.png" alt="Weather icon">
    {% endif %}
</body>
</html>


