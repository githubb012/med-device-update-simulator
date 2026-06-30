from fastapi import FastAPI 
from database import init_db, check_alerts, seed_data, acknowledge_alerts, stop_delivery_db, start_delivery_db
from services.device_service import start_update



init_db()
seed_data()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Device Update Simulator Running"}



@app.post("/start-update")
def start_update_route():
    return start_update()


@app.get("/debug-state")
def debug_state():
    alerts = check_alerts()

    return {
        "active_alerts": len(alerts),
        "system_status": "DEGRADED" if alerts else "OK"
    }


@app.post("/ack-alert")
def ack_alert():

    acknowledge_alerts()

    return {"status": "alert acknowledged"}


@app.post("/stop-delivery")
def stop_delivery():

    stop_delivery_db()

    return {
        "status": "delivery stopped",
        "incident": "alert triggered"
    }

@app.post("/start-delivery")
def start_delivery():

    start_delivery_db()

    return {
        "status": "delivery started"
    }