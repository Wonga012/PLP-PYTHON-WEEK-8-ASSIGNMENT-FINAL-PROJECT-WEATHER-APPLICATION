import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:weather_application/models/weather.dart';

class WeatherProvider with ChangeNotifier {
  List<Weather> _weatherList = [];
  bool _isLoading = false;
  String? _error;

  List<Weather> get weatherList => _weatherList;
  bool get isLoading => _isLoading;
  String? get error => _error;

  Future<void> fetchWeather() async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      final response = await http.get(Uri.parse('http://localhost:3000/api/weather'));
      
      if (response.statusCode == 200) {
        final Map<String, dynamic> data = json.decode(response.body);
        _weatherList = data.entries
            .map((entry) => Weather.fromJson(entry.key, entry.value))
            .toList();
      } else {
        _error = 'Failed to load weather data';
      }
    } catch (e) {
      _error = e.toString();
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}