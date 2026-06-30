import sqlite3


def get_connection():
    conn = sqlite3.connect("device.db")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Devices Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        delivery_active BOOLEAN
    )
    """)

    # 2. Alerts Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        message TEXT,
        acknowledged BOOLEAN
    )
    """)

    # 3. Updates Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS updates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


def check_alerts():
    conn = get_connection()
    cursor = conn.cursor()  # Fetch unresolved alerts (SQLite uses 0/1 for boolean values)
                            # Unresolved alerts block the update workflow
    cursor.execute("""
    SELECT * FROM alerts
    WHERE acknowledged = 0    
    """) 

    results = cursor.fetchall()  # Load query results into memory for alert state evaluation.

    conn.close()

    return results


def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Device
    cursor.execute("""
    INSERT OR REPLACE INTO devices (id, name, delivery_active)
    VALUES (1, 'Pump A', 1)
    """)

    # Alert (initially active - Blocker)
    cursor.execute("""
    INSERT OR REPLACE INTO alerts (id, device_id, message, acknowledged)
    VALUES (1, 1, 'Occlusion detected', 0)
    """)

    # Update state
    cursor.execute("""
    INSERT OR REPLACE INTO updates (id, device_id, status)
    VALUES (1, 1, 'blocked')
    """)


    conn.commit()
    conn.close()


def acknowledge_alerts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE alerts
    SET acknowledged = 1
    WHERE acknowledged = 0 
    """)

    conn.commit()
    conn.close()


def stop_delivery_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE devices
    SET delivery_active = 0
    WHERE id = 1 
    """)

    cursor.execute("""
    INSERT INTO alerts (device_id, message, acknowledged)
    VALUES (1, 'Delivery stopped alert', 0)
    """)

    conn.commit()
    conn.close()

def start_delivery_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE devices
    SET delivery_active = 1
    WHERE id = 1
    """)

    conn.commit()
    conn.close()






