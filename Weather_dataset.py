# IMPORT LIBRARIES

import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# PAGE CONFIGURATION

st.set_page_config(page_title="Weather Dashboard", layout="wide")


# TIME-BASED BACKGROUND

hour = datetime.now().hour

if 5 <= hour < 12:
    page_bg = "#E3F2FD"
elif 12 <= hour < 17:
    page_bg = "#FFF8E1"
elif 17 <= hour < 20:
    page_bg = "#FFE0B2"
else:
    page_bg = "#263238"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
    }}
    .metric-box {{
        padding: 10px;
        border-radius: 12px;
        text-align: center;
        color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        margin-bottom: 20px;   /*  SPACING FIX */
    }}
    </style>
    """,
    unsafe_allow_html=True
)


# TITLE & SUBTITLE

st.markdown("<h1 style='text-align:center;'>🌦 Live Weather Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Real-time Weather Monitoring using Python</h4>", unsafe_allow_html=True)


# SLICERS

s1, s2, s3 = st.columns(3)

with s1:
    city = st.selectbox("🌍 City", ["Chennai", "Bangalore", "Delhi", "Mumbai", "Hyderabad"])

with s2:
    unit = st.selectbox("🌡 Temperature Unit", ["Celsius", "Fahrenheit"])

with s3:
    theme = st.selectbox("🎨 Chart Theme", ["Light", "Dark"])


# API CONFIGURATION

api_key = "e1c0b441e48a22b7f4f55eeabbe21c59"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
data = requests.get(url).json()


# EXTRACT WEATHER DATA

temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
wind = data["wind"]["speed"]
lat = data["coord"]["lat"]
lon = data["coord"]["lon"]

sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")

if unit == "Fahrenheit":
    temp = (temp * 9/5) + 32
    feels_like = (feels_like * 9/5) + 32


# KPI CARDS

k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(f"<div class='metric-box' style='background:#ef5350;'><h4>Temperature</h4><h2>{round(temp,1)}</h2></div>", unsafe_allow_html=True)
with k2:
    st.markdown(f"<div class='metric-box' style='background:#ab47bc;'><h4>Feels Like</h4><h2>{round(feels_like,1)}</h2></div>", unsafe_allow_html=True)
with k3:
    st.markdown(f"<div class='metric-box' style='background:#26a69a;'><h4>Humidity</h4><h2>{humidity}%</h2></div>", unsafe_allow_html=True)
with k4:
    st.markdown(f"<div class='metric-box' style='background:#42a5f5;'><h4>Wind</h4><h2>{wind} m/s</h2></div>", unsafe_allow_html=True)
with k5:
    st.markdown(f"<div class='metric-box' style='background:#ffa726;'><h4>Pressure</h4><h2>{pressure}</h2></div>", unsafe_allow_html=True)

# EXTRA GAP BELOW KPI ROW
st.markdown("")

# DATAFRAME
df = pd.DataFrame({
    "Metric": ["Temperature", "Feels Like", "Humidity", "Pressure", "Wind Speed"],
    "Value": [temp, feels_like, humidity, pressure, wind]
})


# CHART FUNCTION

def chart(title):
    fig, ax = plt.subplots(figsize=(4,3))
    ax.set_title(title)
    return fig, ax


# MAIN DIVISION (LEFT & RIGHT)

left, right = st.columns([1.5, 2.0])

# LEFT SIDE
with left:
    st.markdown("### 🗺️ City Location")
    st.map(pd.DataFrame({"lat":[lat], "lon":[lon]}), zoom=6)

    st.markdown(
        f"""
        <div class='metric-box' style='background:#ffb300;margin-top:20px;'>
        <h4>🌅 Sun Timings</h4>
        <h3>Sunrise: {sunrise}</h3>
        <h3>Sunset: {sunset}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

# RIGHT SIDE (6 CHARTS) 
r1, r2 = right.columns(2)

with r1:
    fig, ax = chart("Trend Analysis")
    ax.plot(df["Metric"], df["Value"], marker="o")
    st.pyplot(fig)

with r2:
    fig, ax = chart("Value Comparison")
    sns.barplot(x="Metric", y="Value", data=df, ax=ax)
    st.pyplot(fig)

r3, r4 = right.columns(2)

with r3:
    fig, ax = chart("Proportion View")
    ax.pie(df["Value"], labels=df["Metric"], autopct="%1.1f%%")
    st.pyplot(fig)

with r4:
    fig, ax = chart("Rank Comparison")
    ax.barh(df["Metric"], df["Value"])
    st.pyplot(fig)

r5, r6 = right.columns(2)

with r5:
    fig, ax = chart("Volume Change")
    ax.fill_between(df["Metric"], df["Value"], alpha=0.5)
    st.pyplot(fig)

with r6:
    fig, ax = chart("Distribution Pattern")
    ax.hist(df["Value"], bins=5)
    st.pyplot(fig)

