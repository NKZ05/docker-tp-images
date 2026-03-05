const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;

const cities = {
  paris: { temp: 18, weather: 'nuageux' },
  lyon: { temp: 22, weather: 'ensoleillé' },
  marseille: { temp: 25, weather: 'ensoleillé' }
};

app.get('/api/weather/:city', (req, res) => {
  const city = req.params.city.toLowerCase();
  const data = cities[city];

  if (data) {
    res.json({ city, ...data });
  } else {
    res.status(404).json({ error: 'Ville non trouvée' });
  }
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.listen(PORT, () => {
  console.log(`API météo sur le port ${PORT}`);
});
