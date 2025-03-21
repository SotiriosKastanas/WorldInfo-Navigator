# 🌍 WorldInfo-Navigator

An **AI-powered multi-agent system** built with **AutoGen** that provides **real-time weather, time zones, and country information**. This project demonstrates how AI agents can **collaborate and retrieve information** dynamically from external APIs.

📖 **Read the Full Article on Medium:**  
[👉 Building an AI-Powered Multi-Agent System with AutoGen](https://medium.com/@Sotirios_Kastanas/building-an-ai-powered-multi-agent-system-with-autogen-7fe69e4bc5cd) 
---

## 🚀 Features
- 🌦️ **Weather Agent** – Fetches real-time weather data using [OpenWeather API](https://openweathermap.org/api)
- 🕒 **Time Zone Agent** – Provides accurate time zone information using [Google Time Zone API](https://developers.google.com/maps/documentation/timezone/start)
- 🌍 **Country Info Agent** – Retrieves country-specific details using [RestCountries API](https://restcountries.com/)
- 🤖 **Orchestrator** – Routes user queries to the appropriate agent(s) dynamically

---

## 📺 Demo Video
🎥 **Watch the project in action**:  

https://github.com/user-attachments/assets/785e6ed3-0aaf-40e1-becc-93d313c842c7

---

## 🔧 Installation
To set up **WorldInfo-Navigator** on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/WorldInfo-Navigator.git
   cd WorldInfo-Navigator
   pip install -r requirements.txt

2. **How to Run**:
   ```bash
   cd src
   streamlit run User_Interface/app.py
