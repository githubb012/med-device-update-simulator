from database import check_alerts
from logger import log_event

def start_update():

    alerts = check_alerts()

    if alerts:
        log_event("Update blocked because active alerts exist")
        
        return{
            "status": "BLOCKED",
            "reason": "Active alerts detected",
            "next_step": "Acknowledge alerts before update"
        }
    
    log_event("Update started successfully")

    return {
        "status": "SUCCESS",
        "message": "Update started"
    }

