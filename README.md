'CHAD-BOT' Discord Automated Bot

# Discord Weather Comparison Bot

A Python-based Discord bot with multi-functionality for customized actions for users within a server. 

MORE UPDATES AND FEATURES COMING SOON

---

##  Features

*  **Multi-City Weather Comparison**

  * Compares real-time weather between St. Louis, MO and Milwaukee, WI
*  **Detailed Weather Data**

  * Temperature (°F)
  * Humidity
  * Daily High / Low
  * Chance of Rain
  * Weather Conditions (translated from API codes)
*  **Smart Alert System**

  * Detects severe weather conditions such as:

    * Thunderstorms
    * Heavy rain
    * High precipitation probability
*  **Discord Slash Command Integration**

  * Use `/weather` to trigger reports instantly
*  **Automated Startup & Recovery**

  * Runs automatically via Windows Task Scheduler
  * Restarts on failure for high reliability

---

##  Tech Stack

* **Python 3**
* **discord.py** — Discord bot framework
* **requests** — API calls
* **Open-Meteo API** — Weather data provider
* **python-dotenv** — Environment variable management
* **Windows Task Scheduler** — Automation & uptime

---

##  Project Structure

```
weather_discord_bot/
├── bot.py                # Discord bot interface
├── weather_service.py   # Core weather logic & API handling
├── requirements.txt     # Dependencies
├── .env                 # Environment variables (not committed)
└── run_bot.bat          # Optional startup script
```

---

##  Setup Instructions

### 1. Clone or Download the Repository

```bash
git clone https://github.com/yourusername/weather_discord_bot.git
cd weather_discord_bot
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
DISCORD_TOKEN=your_discord_bot_token
```

---

### 4. Run the Bot

```bash
python bot.py
```

You should see:

```text
Logged in as YOUR-BOT-NAME
```

---

### 5. Use in Discord

In your server:

```text
/weather
```

---

## How It Works

1. Bot receives a `/weather` command
2. Calls Open-Meteo API for each city
3. Processes and aggregates weather data
4. Translates weather codes into readable descriptions
5. Applies alert logic based on conditions
6. Sends formatted report back to Discord

---

##  Automation (Windows)

This project is configured to run as a background service using **Task Scheduler**:

* Starts automatically on login or system startup
* Restarts if the bot crashes
* Runs without requiring an open terminal

---

##  Example Output

![Weather Output](README/ExampleWeather.png)

```
Weather Report

St. Louis
Current Temp: 61.3°F
Conditions: Overcast
Humidity: 58%
High: 65.2°F
Low: 52.1°F
Chance of Rain: 40%
Alert: No severe alerts

Milwaukee
Current Temp: 60.5°F
Conditions: Slight rain
Humidity: 64%
High: 63.0°F
Low: 50.4°F
Chance of Rain: 70%
Alert: ⚠️ High Chance of Rain

Comparison Summary
Warmer City: St. Louis
More Humid City: Milwaukee
Bigger Temperature Swing: St. Louis
```

---

## Future Improvements

* User-selected cities via command input
* Scheduled daily weather reports
* Push notifications for severe weather alerts
* Cloud deployment (Render, Railway, or Cloud Run)
* Web API version using FastAPI
* 24/7 functionality via dedicated server

---

## Portfolio Summary

Built a Python-based Discord bot that integrates with a live weather API, processes multi-city data, generates intelligent weather alerts, and delivers formatted reports via slash commands. Designed with modular architecture and deployed as an automated background service using Windows Task Scheduler.

---

## License

This project is open-source and available for personal or educational use.

---

## Author

Nicholas Henslow Schrang
Developer
