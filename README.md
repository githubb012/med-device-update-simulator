
# 🏥 Medical Device Update Simulator (Insulin Pump Safety System)

---

## 🚀 Overview

This project is a **medical device update simulation system** inspired by insulin pump safety-critical workflows.

It models how software updates are controlled in regulated environments where device state, safety alerts, and operational constraints determine whether an update can proceed.

The system simulates real-world constraints found in **medical device ecosystems (e.g. insulin pump software platforms)** where updates must never compromise patient safety.

---

## 🎯 Problem Statement

In safety-critical medical systems, software updates cannot be applied freely. They must be gated by:

- Active safety alerts
- Device operational state (e.g. delivery running/stopped)
- System health conditions
- Incident history

This project simulates that decision-making layer.

---

## 🏗️ System Architecture

```text
Streamlit Frontend
        ↓
FastAPI Backend (API Layer)
        ↓
Service Layer (Business Logic)
        ↓
SQLite Database Layer
        ↓
Logging System (Audit Trail)

```

## Project Structure

```

med-device-update-simulator/
│
├── app.py
├── database.py
├── streamlit_app.py
├── logger.py
│
├── services/
│   └── device_service.py
│
├── logs/
│   └── events.log
│
├── tests/
├
├── requirements.txt
└── README.md

```
---


## Core Features

🔹 Device State Simulation  
- Start and stop insulin delivery  
- Persist device state in SQLite
- Simulate operational changes before software updates

🔹 Safety Alert System  
- Active alerts prevent software updates
- Alerts must be acknowledged before updates can proceed
- Safety checks mimic regulated medical device workflows

🔹 Update Control Engine  
The `/start-update` endpoint evaluates the current system state.

Possible outcomes:  
- **BLOCKED** - One or more active alerts exist
- **SUCCESS** - The system passes all safety checks

🔹 Operational Dashboard
Built using Streamlit
Real-time system state visibility
Control buttons for operations
API-driven interactions  

```
## 🧠 Business Logic 

The similator follows a safety-first workflow.

Rules:

- If active_alerts > 0, updates are blocked.
- If active_alerts == 0, updates are permitted.

Additional constraints:

- Stopping delivery automatically creates an alert.
- Alerts must be acknowledged before updates can continue.

```
---


```
## 🧱 Tech Stack
- Backend: FastAPI  
- Frontend: Streamlit  
- Database: SQLite  
- Language: Python  
- Architecture: Layered (API → Service → Database)  
- Logging: File-based audit logging

```
---

## Additional constraints:

Delivery stop triggers alert generation
Alerts must be acknowledged before system recovery

```

## 🚧 Current Status

Sprint 1 completed

Implemented:

- FastAPI REST API
- SQLite database
- Streamlit dashboard
- Service layer
- Logging
- Git version control

Next sprint:

- Docker
- pytest
- Postman
- GitHub Actions

```

