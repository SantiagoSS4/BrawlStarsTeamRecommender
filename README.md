# BrawlStarsTeamRecommender
Sistema de recomendación de equipos en Brawl Stars

Este proyecto utiliza redes bayesianas para recomendar equipos competitivos en Brawl Stars basándose en roles, probabilidades de desempeño y sinergias entre personajes. Además, permite simular partidas y actualizar probabilidades dinámicamente según los resultados obtenidos.

🚀 Características
Recomendación de equipos: Selección de equipos de tres personajes optimizados para un mapa específico.
Red bayesiana: Cálculo de probabilidades basado en características como vida, daño, rango, etc.
Sinergias: Evaluación de sinergias entre personajes para ajustar probabilidades.
Simulación de partidas: Actualización de probabilidades de mapa según el resultado de la partida.
Gráfico de la red bayesiana: Representación visual de la red bayesiana generada.

📂 Estructura del proyecto
├── Datos.py         # Maneja la lectura y categorización de datos.
├── RedBayesiana.py # Configura y grafica la red bayesiana.
├── Equipos.py         # Genera combinaciones y evalúa equipos.
├── Feedback.py     # Simula partidas y actualiza probabilidades.
├── BSlogica.py               # Maneja las sinergias entre personajes.
├── Main.py                   # Archivo principal que integra todos los módulos.
├── base_datos_brawlstars.csv # Archivo CSV con los datos iniciales de personajes.

