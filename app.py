import streamlit as st
from tools import get_coordinates, get_weather

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Weather Information Agent",
    page_icon="🌦️",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌦️ Weather Information Agent")
st.markdown(
    """
This application retrieves the **current weather information** for a given city
using the **Open-Meteo Geocoding API** and **Open-Meteo Weather API**.
"""
)

st.divider()

# -----------------------------
# User Input
# -----------------------------
city = st.text_input(
    "City Name",
    placeholder="Enter a city (e.g., Chennai)"
)

# -----------------------------
# Search Button
# -----------------------------
if st.button("Get Weather Information", use_container_width=True):

    if city.strip() == "":
        st.warning("Please enter a city name.")
    else:

        coordinates = get_coordinates(city)

        if isinstance(coordinates, str):
            st.error(coordinates)

        else:

            latitude = coordinates["latitude"]
            longitude = coordinates["longitude"]

            weather = get_weather(latitude, longitude)

            if isinstance(weather, str):
                st.error(weather)

            else:

                st.success("Weather information retrieved successfully.")

                with st.container(border=True):

                    st.subheader("Location Details")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric("City", coordinates["city"])
                        st.metric("Latitude", latitude)

                    with col2:
                        st.metric("Longitude", longitude)

                st.write("")

                with st.container(border=True):

                    st.subheader("Current Weather")

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.metric(
                            label="Temperature",
                            value=f"{weather['temperature']} °C"
                        )

                    with col2:
                        st.metric(
                            label="Humidity",
                            value=f"{weather['humidity']} %"
                        )

                    with col3:
                        st.metric(
                            label="Wind Speed",
                            value=f"{weather['wind_speed']} km/h"
                        )