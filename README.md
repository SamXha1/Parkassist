# 🚗 ParkAssist – Smart Parking Management System

## 📌 Project Overview

**ParkAssist** is a smart parking management system designed to help drivers quickly locate available parking spaces in urban areas. The project combines **IoT hardware** and **web-based software** to monitor parking slot availability in real time and provide navigation to the selected parking location. By reducing the time spent searching for parking, ParkAssist helps decrease traffic congestion, fuel consumption, and driver frustration.

---

# ✨ Key Features

- 🚗 Real-time parking slot detection
- 📍 Live parking availability monitoring
- 🗺️ Map-based navigation to available parking spaces
- 📡 IoT-based communication using ESP32
- 🌐 Web dashboard for parking management
- 📱 User-friendly interface for drivers
- ⚡ Fast and efficient parking slot updates

---

# 🛠️ Hardware Components

The hardware section of the project is responsible for detecting vehicle presence and sending parking status to the server.

### Components Used

- Arduino Uno
- ESP32 Wi-Fi Module
- IR Sensors
- Breadboard/Extension Board
- Jumper Wires
- Power Supply

### Hardware Working

- IR sensors detect whether a parking slot is occupied.
- Arduino Uno processes the sensor readings.
- ESP32 transmits parking slot status over Wi-Fi.
- The server updates the parking availability in real time.
- Drivers can view available slots through the web application.

---

# 💻 Software Components

The software section manages parking data, user interaction, and navigation services.

### Technologies Used

- Python
- Flask Framework
- HTML
- CSS
- JavaScript
- MySQL Database
- Google Maps API (Map API)

---

# ⚙️ Software Workflow

1. IR sensors detect vehicle presence.
2. Arduino Uno collects sensor data.
3. ESP32 sends data to the Flask server.
4. Flask processes and stores the data in MySQL.
5. The web application displays available parking spaces.
6. Google Maps API provides navigation to the selected parking location.

---

# 🏗️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python, JavaScript |
| Frontend | HTML, CSS, JavaScript |
| Backend | Flask |
| Database | MySQL |
| IoT | Arduino Uno, ESP32 |
| Sensors | IR Sensors |
| API | Google Maps API |

---

# 🚀 Project Benefits

- Reduces time spent searching for parking.
- Minimizes traffic congestion.
- Saves fuel and travel time.
- Provides real-time parking availability.
- Easy to deploy in urban parking areas.
- Cost-effective IoT-based smart parking solution.

---

# 📈 Future Enhancements

- Mobile application (Android/iOS)
- Online parking reservation
- QR code-based parking entry
- Digital payment integration
- AI-based parking demand prediction
- CCTV integration for security
- Vehicle number plate recognition (ANPR)

---

# 👨‍💻 Developed Using

- Arduino Uno
- ESP32
- Python
- Flask
- HTML
- CSS
- JavaScript
- MySQL
- Google Maps API
- IR Sensors

---

## 📄 Conclusion

ParkAssist is an IoT-enabled smart parking solution that integrates hardware and software to provide real-time parking space detection and navigation. The system improves parking efficiency, reduces congestion in urban areas, and offers a scalable solution for smart city infrastructure.
