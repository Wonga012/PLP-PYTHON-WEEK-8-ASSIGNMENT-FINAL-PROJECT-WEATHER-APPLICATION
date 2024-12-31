import express from 'express';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import { weatherData } from './weather-data.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const port = 3000;

// Serve static files
app.use(express.static(__dirname));

// Weather API endpoint
app.get('/api/weather', (req, res) => {
  res.json(weatherData);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});