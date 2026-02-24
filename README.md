# 🏥 AI-Powered Patient Fall Detection System

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv8-Real--Time-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/OpenCV-Video%20Processing-green?style=for-the-badge&logo=opencv"/>
  <img src="https://img.shields.io/badge/Flask-Web%20Backend-black?style=for-the-badge&logo=flask"/>
  <img src="https://img.shields.io/badge/Status-Version%201.0-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  <b>A real-time AI-powered patient monitoring system that detects falls instantly and alerts healthcare staff — built with YOLOv8, Flask, and a hospital-grade live dashboard.</b>
</p>

---

![Image](https://github.com/user-attachments/assets/38017ba6-47a7-4667-9adb-467d6cccb1fe)


## 🚨 The Problem

Falls are among the **leading causes of preventable injury** in hospitals, elder-care facilities, and rehabilitation centers worldwide.

- Every **11 seconds**, an older adult is treated in the ER for a fall-related injury
- Hospital falls cost the US healthcare system **$50 billion annually**
- Up to **30% of in-hospital falls** result in serious injury
- Nursing staff cannot watch every patient simultaneously

**Current solutions rely on call buttons and periodic checks — both reactive, not preventive.**

This project is a step toward making patient monitoring proactive, intelligent, and automatic.

---

## 🎯 What This System Does

HemaVision detects patient falls the moment they happen — from a live camera feed — and immediately triggers a visual alert on a medical dashboard, enabling faster staff response.

```
📷 Camera Feed
      ↓
🎞️  OpenCV Video Capture
      ↓
🧠  YOLOv8 Inference Engine
      ↓
⚖️  Fall Classification Logic
      ↓
🖥️  Flask Backend Server
      ↓
🚨  Live Dashboard — SAFE / FALL Alert
```

---

## 🧠 Tech Stack

| Component | Technology | Role |
|-----------|-----------|------|
| Object Detection | **YOLOv8** | Real-time fall detection inference |
| Video Processing | **OpenCV** | Camera capture & frame processing |
| Backend Server | **Flask** | API, video streaming, state management |
| Frontend UI | **HTML / CSS / JS** | Live medical alert dashboard |
| Core Logic | **Python** | System orchestration |

---

## ✨ Key Features

- ✅ **Real-time fall detection** from live camera feed
- ✅ **YOLOv8 bounding-box annotations** overlaid on live stream
- ✅ **Animated SAFE / FALL status display** with instant UI state change
- ✅ **Hospital-grade responsive dashboard** — clean, minimal, distraction-free
- ✅ **Backend–Frontend real-time synchronization** via Flask streaming
- ✅ **Zero-lag alert triggering** — detection to alert in milliseconds

---

## 🏥 Why This Matters for Healthcare

| Impact | Detail |
|--------|--------|
| ⏱ **Faster Response** | Staff are alerted the instant a fall occurs, not minutes later |
| 🛑 **Injury Prevention** | Immediate response reduces severity of fall-related complications |
| 👵 **Vulnerable Patient Care** | Designed for elderly, post-surgery, and high-fall-risk patients |
| 👩‍⚕️ **Staff Support** | Reduces cognitive load on overburdened nursing teams |

**Potential Deployment Contexts:**
- Hospital ward monitoring assistant
- Elder-care & nursing home surveillance
- Smart ICU monitoring module
- Rehabilitation center patient supervision
- Post-operative recovery room monitoring

---

## 💻 Why This Matters for Engineers

This project demonstrates several production-grade engineering patterns:

- ⚡ **Real-time AI inference** — YOLOv8 running at video framerate in a web context
- 🌐 **Streaming AI over web** — Flask multipart streaming for live video delivery
- 🔄 **Backend–Frontend sync** — real-time state propagation without WebSockets
- 🧩 **Human-centric AI design** — building AI systems around clinical workflows
- 🎯 **Applied Computer Vision** — moving from benchmark datasets to real-world deployment

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-fall-detection.git
cd ai-fall-detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your YOLOv8 Weights
Place your trained `best.pt` weights file in the project root:
```
ai-fall-detection/
├── main.py
├── best.pt        ← your trained YOLOv8 weights here
├── templates/
│   └── index.html
└── requirements.txt
```

### 4. Run the System
```bash
python main.py
```

### 5. Open the Dashboard
```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
ai-fall-detection/
├── main.py               # Flask app — video stream, inference, alert API
├── templates/
│   └── index.html        # Animated medical dashboard UI
├── static/               # CSS, JS assets
├── requirements.txt      # Dependencies
└── README.md
```

---

## 📦 Requirements

```
ultralytics>=8.0.0
opencv-python>=4.8.0
flask>=2.3.0
numpy>=1.24.0
torch>=2.0.0
```

---

## 🛠️ Version 1.0 — Current Capabilities

- [x] Single-patient real-time monitoring
- [x] Live camera detection with bounding boxes
- [x] Immediate visual SAFE / FALL alert trigger
- [x] Real-time UI state change on fall event
- [x] Live video stream in browser dashboard

---

## 🔮 Roadmap — Planned Upgrades

| Version | Feature |
|---------|---------|
| v1.1 | **Pose-based fall detection** using skeleton keypoints (higher accuracy, fewer false alarms) |
| v1.2 | **Fall confirmation logic** — temporal smoothing to eliminate single-frame false positives |
| v1.3 | **Sound + SMS alerts** to nursing stations via Twilio integration |
| v2.0 | **Multi-patient dashboard** — simultaneous monitoring of multiple rooms/beds |
| v2.1 | **Fall history logging** — timestamped event log with annotated frames |
| v2.2 | **Analytics module** — fall frequency charts, high-risk time analysis |
| v3.0 | **Cloud deployment** — scalable hospital network architecture |
| v3.1 | **EHR integration** — automatic fall event logging to patient records |

---

## 🌍 Long-Term Vision

Build a **scalable AI-powered hospital monitoring platform** capable of:

- 📹 Multi-camera infrastructure across entire wards
- 🔔 Smart predictive alerts before a fall occurs (using gait analysis)
- 🖥️ Centralized hospital command dashboard
- ☁️ Cloud-based monitoring with role-based access for staff
- 📊 Population-level fall analytics for hospital safety officers

The goal is not to replace nursing staff — it is to give them a second set of eyes that never blinks.

---

## 🤝 Open to Collaboration

I would love to connect and collaborate with:

- 👨‍⚕️ **Doctors & clinicians** interested in AI-assisted patient monitoring
- 🧬 **Biomedical engineers** working on smart hospital infrastructure
- 🚀 **Healthcare startups** building patient safety products
- 🔬 **Computer vision researchers** focused on human action recognition
- 🏥 **Hospital IT teams** exploring AI integration

**Let's build safer hospitals using AI.**

📧 Reach out via [LinkedIn](https://www.linkedin.com/in/mansoor-alam-085b19116/) or open an issue on this repo.

---

## 📜 License

This project is open-source under the **MIT License** — free to use, modify, and build upon with attribution.

---

## ⭐ Support This Project

If you find this useful or inspiring:

- ⭐ **Star** this repository
- 🍴 **Fork** it and build on top of it
- 💬 **Open an issue** with feedback or ideas
- 📤 **Share** it with someone in healthcare or AI

> *"The best technology in healthcare is invisible — it just keeps patients safe."*

---
