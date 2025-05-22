# Eye Tracking Cursor Control Web App

This project is a full-stack implementation of a real-time eye-tracking web application that captures webcam input from the frontend and processes it using computer vision techniques on the backend to control the mouse cursor via gaze direction and wink detection.

## 🔍 Features

- Real-time webcam frame capture using HTML5 and JavaScript
- Backend processing using Python (Flask + OpenCV)
- Eye landmark detection and gaze tracking
- Wink detection for left/right click simulation
- PyAutoGUI integration to control the system cursor
- Smooth frontend-backend integration with JSON API
- Responsive and accessible user interface

## 🛠 Tech Stack

- **Frontend**: HTML5, JavaScript, CSS
- **Backend**: Python, Flask, OpenCV
- **Computer Vision**: MediaPipe-based facial landmark detection
- **Mouse Control**: PyAutoGUI
- **Communication**: JSON over HTTP (Fetch API)

## 🚀 Project Structure
```
project/
│
├── static/ # Frontend JS script
│ └── script.js
│
├── templates/ # HTML template
│ └── index.html
│
├── modules/ # Detection and tracking logic
│ ├── detector.py
│ ├── gaze_tracker.py
│ ├── wink_detector.py
│ └── controller.py
│
├── app.py # Flask application entry point
└── README.md # Project documentation
```


## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/Jitenrai21/EyeTrackingApp
cd EyeTrackingApp
```
Install dependencies

```bash
pip install -r requirements.txt
```

Run the application
```bash
python -m web.app
```

Access the app
Open your browser and go to: http://localhost:5000

## 📸 How It Works
- The frontend captures webcam frames using the HTML5 video API and sends them to the backend every 200ms.
- The backend decodes the image, detects facial landmarks, and estimates gaze direction and wink.
- Based on the estimation, the system cursor is moved or mouse clicks are triggered.

## 🎯 Goals and Insights
- Understanding the integration between frontend and backend systems was key to making this project production-ready. It demonstrates how aligning real-time UI input with backend intelligence enables fluid, responsive applications.
