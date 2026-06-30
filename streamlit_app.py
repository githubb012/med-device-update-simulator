import streamlit as st
import requests


BASE_URL = "http://127.0.0.1:8000"

st.title("Device Incident Loop Simulator")

# -------------------------------------------
# SYSTEM STATE
# -------------------------------------------

st.header ("System State")

try:
    debug = requests.get(f"{BASE_URL}/debug-state").json()

    st.write("### Active Alerts")
    st.write(debug["active_alerts"])

    st.write("### System Status")
    st.write(debug["system_status"])

except Exception as e:
    st.error(f"Backend connection failed: {e}")


# -------------------------------------------------
# CONTROL BUTTONS
# -------------------------------------------------

st.header("Controls")

col1, col2, col3, col4 = st.columns(4)

# STOP DELIVERY 
with col1:
    if st.button("Stop Delivery"):
        response = requests.post(f"{BASE_URL}/stop-delivery")
        st.success(response.json())

# START DELIVERY
with col2:
    if st.button("Start Delivery"):
        response = requests.post(f"{BASE_URL}/start-delivery")
        st.success(response.json())

# ACKNOWLEDGE ALERT
with col3:
    if st.button("Acknowledge Alert"):
        response = requests.post(f"{BASE_URL}/ack-alert")
        st.success(response.json())
    
# START UPDATE
with col4:
    if st.button("Start Update"):
        response = requests.post(f"{BASE_URL}/start-update")
        st.success(response.json())

# --------------------------------------------------
# INDCIDENT EXPLANATION
# --------------------------------------------------


st.header("Incident Workflow")

st.info("""
This simulator demonstrates a healthcare device update loop:
        
1. Insulin delivery must stop before update
2. Stopping delivery triggers a safety alert
3. Active alerts blocks software update
4. Engineers acknowledge alerts
5. Delivery restart may recreate the loop
""")




st.write("Streamlit is working.")
