# 🌦️ Weather Information AI Agent

## Overview

The Weather Information AI Agent is a Python-based intelligent assistant that provides real-time weather information for cities using the Open-Meteo Geocoding API and Open-Meteo Weather API. It uses an AI model through OpenRouter with tool-calling capabilities to retrieve live weather data and generate natural language responses.

The agent can answer questions about a city's current temperature, humidity, wind speed, and geographical coordinates.

---

## Features

* AI-powered weather information assistant
* Tool calling using OpenRouter
* Fetches live weather information using Open-Meteo APIs
* Automatically converts city names into geographical coordinates
* Uses external API integration
* Supports conversational interactions
* Stores conversation history using memory
* Easy to extend with additional weather tools

---

## Technologies Used

* Python
* OpenRouter API
* Open-Meteo Geocoding API
* Open-Meteo Weather API
* Requests
* Python Dotenv

---

## Project Structure

```text
weather_information_agent/
│
├── main.py          # Main agent loop
├── tools.py         # Weather tools
├── prompts.py       # System prompt
├── memory.py        # Conversation memory
├── .env             # API key
├── memory.json      # Stores conversation history
└── README.md
```

---

### Install dependencies

```bash
pip install requests python-dotenv
```

---

## Environment Variables

Create a `.env` file and add:

```text
OPENROUTER_API_KEY=your_openrouter_api_key
```

> **Note:** Open-Meteo APIs do not require an API key.

---

## Running the Project

```bash
python main.py
```

---

## Example Questions

* What is the weather in Chennai?
* Tell me the current weather in London.
* Show me the weather in Tokyo.
* What is the temperature in New York?
* What is the humidity in Paris?
* What is the wind speed in Sydney?

---

## Workflow

1. User enters a weather-related question.
2. The AI model receives the request.
3. The model calls the `get_coordinates()` tool to obtain the city's latitude and longitude.
4. The Geocoding API returns the geographical coordinates.
5. The model calls the `get_weather()` tool using those coordinates.
6. The Weather API returns the current weather information.
7. The AI model generates a natural-language response.
8. The response is displayed to the user.

---

## Example Output

```text
User:
What is the weather in Chennai?

Agent:
The current weather in Chennai is:

Temperature: 33.7 °C
Humidity: 49%
Wind Speed: 10 km/h
```

---

## Future Improvements

* 7-day weather forecast
* Hourly weather forecast
* Air Quality Index (AQI)
* UV Index information
* Sunrise and sunset timings
* Voice-based interaction
* Multi-language support
* Export weather reports as PDF
* Cache API responses for faster performance

---

## Author

Developed as an AI Agent project using Python, OpenRouter, Open-Meteo Geocoding API, and Open-Meteo Weather API.
