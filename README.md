🌦 Live Weather Analytics Dashboard
A Streamlit-based web application that shows real-time weather data using the OpenWeather API, visualized through multiple charts and an interactive UI.

Features
✔ Live weather data via OpenWeather API
✔ Location map using latitude & longitude
✔ Dynamic background (based on time of day)
✔ KPI cards (Temperature, Humidity, Wind, Pressure, Feels Like)
✔ 6 different chart views:
Line Chart
Bar Chart
Pie Chart
Horizontal Bar
Area Chart
Histogram
✔ City & unit selection (°C / °F)
✔ Clean UI with CSS styling

Tech Stack
Component	   Technology
Backend	     Python
Frontend	   Streamlit
API	         OpenWeatherMap
Charts	     Matplotlib, Seaborn
Data	       Pandas

Installation & Setup
1️. Clone the repository
git clone https://github.com/your-username/weather-dashboard.git
cd weather-dashboard

2️. Install dependencies
pip install -r requirements.txt

3️. Add API Key
Get an API key from OpenWeather → https://openweathermap.org/
Edit the script and replace:
api_key = "YOUR_API_KEY"

4️. Run the App
streamlit run app.py

📁 Folder Structure
weather-dashboard
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┗ 📜 README.md

Screenshots:
![Screenshot_21-1-2026_102057_localhost](https://github.com/user-attachments/assets/cad73a25-323d-498a-be01-8f0eb29c7ea7)
![Screenshot_21-1-2026_10223_localhost](https://github.com/user-attachments/assets/b5629f03-55c1-4d68-8007-11de1a7b25e1)


Requirements:
Create a requirements.txt like this:
streamlit
requests
pandas
matplotlib
seaborn

API Provider:
This app uses OpenWeatherMap API
Docs: https://openweathermap.org/api

Contributions:
Contributions are welcome!
Fork → Modify → Pull Request 

License:
MIT License © 2026
 
