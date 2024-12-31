import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

# Simulated weather data store
weather_data = {
    "Nairobi": {
        "temperature": 22,
        "humidity": 65,
        "condition": "Partly Cloudy",
        "last_updated": datetime.now().isoformat()
    },
    "Mombasa": {
        "temperature": 29,
        "humidity": 75,
        "condition": "Sunny",
        "last_updated": datetime.now().isoformat()
    },
    "Kisumu": {
        "temperature": 26,
        "humidity": 70,
        "condition": "Clear",
        "last_updated": datetime.now().isoformat()
    }
}

class WeatherHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/weather':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(weather_data).encode())
            return
        
        # Serve the HTML page for root path
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())
            return

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, WeatherHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()