class Weather {
  final String location;
  final double temperature;
  final int humidity;
  final String condition;
  final DateTime lastUpdated;

  Weather({
    required this.location,
    required this.temperature,
    required this.humidity,
    required this.condition,
    required this.lastUpdated,
  });

  factory Weather.fromJson(String location, Map<String, dynamic> json) {
    return Weather(
      location: location,
      temperature: json['temperature'].toDouble(),
      humidity: json['humidity'],
      condition: json['condition'],
      lastUpdated: DateTime.parse(json['last_updated']),
    );
  }
}