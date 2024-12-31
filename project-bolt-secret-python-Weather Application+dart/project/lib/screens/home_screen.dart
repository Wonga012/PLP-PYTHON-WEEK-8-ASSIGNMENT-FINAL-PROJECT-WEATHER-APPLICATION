import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:weather_application/providers/weather_provider.dart';
import 'package:weather_application/widgets/weather_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  void initState() {
    super.initState();
    Future.microtask(
      () => context.read<WeatherProvider>().fetchWeather(),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Weather Application'),
        centerTitle: true,
      ),
      body: Consumer<WeatherProvider>(
        builder: (context, weatherProvider, child) {
          if (weatherProvider.isLoading) {
            return const Center(child: CircularProgressIndicator());
          }

          if (weatherProvider.error != null) {
            return Center(child: Text(weatherProvider.error!));
          }

          return RefreshIndicator(
            onRefresh: weatherProvider.fetchWeather,
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: weatherProvider.weatherList.length,
              itemBuilder: (context, index) {
                final weather = weatherProvider.weatherList[index];
                return WeatherCard(weather: weather);
              },
            ),
          );
        },
      ),
    );
  }
}