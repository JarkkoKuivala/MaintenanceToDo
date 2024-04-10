import sqlite3

create_tables_sql = """CREATE TABLE IF NOT EXISTS Devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name VARCHAR(50),
    model VARCHAR(50),
    user_id KEY
)""", """CREATE TABLE IF NOT EXISTS Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task VARCHAR(50),
    deadline TEXT,
    completed VARCHAR(50),
    repetetive VARCHAR(50),
    take_note VARCHAR(50),
    publishing VARCHAR(50),
    users_id KEY,
    devices_id KEY
)""", """CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50)
)"""

get_tasks_list = ""

def get_connection():
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        return conn
    except:
        print("Failed to connect to database")
    return conn
   
def create_tables():
    conn = get_connection()
    if conn == None:
        return None
    try:
        c = conn.cursor()
        for i in create_tables_sql:
            c.execute(i)
        print("Successfully created tables")
        return "Success"
    except:
        print("Failed to create table")
    return None

def new_user(user):
    conn = get_connection()
    if conn == None:
        return None
    try:
        print (user)
        sql = "INSERT INTO Users (name) VALUES(?)"
        c = conn.cursor()
        c.execute(sql, [user])
        conn.commit()
        return "Success"
    except:
        print ("Failed to add new user")
    return None

def new_device(data):
    conn = get_connection()
    if conn == None:
        return None
    try:
        data_tuple = (data["device_name"], data["model"], data["users_id"])
        
        sql = "INSERT INTO Devices (device_name, model, user_id) VALUES(?,?,?)"
        c = conn.cursor()
        c.execute(sql, data_tuple)
        conn.commit()
        return "Success"
    except:
        print ("Failed to add new device")
    return None

def new_task(data):
    conn = get_connection()
    if conn == None:
        return None
    try:
        data_tuple = (data["task"], data["deadline"], data["device_id"], data["user_id"])
        
        sql = "INSERT INTO Tasks (task, deadline, devices_id, users_id) VALUES(?,?,?,?)"
        c = conn.cursor()
        c.execute(sql, data_tuple)
        conn.commit()
        return "Success"
    except:
        print ("Failed to add new tasks")
    return None

def get_tasks(user_id):
    conn = get_connection()
    if conn == None:
        return None
    try:
        print(user_id)
        id = (user_id["key"])
        print(id)
        sql = """SELECT Tasks.task, Tasks.deadline, Tasks.completed, Tasks.repetetive, Tasks.take_note, Tasks.publishing, Devices.device_name, Devices.model
        FROM Tasks, Devices WHERE Tasks.users_id=? 
        """
        tasks = conn.execute(sql, [id]).fetchall()
        return tasks
    except:
        print ("Failed get tasks")
    return None    


def get_devices(user_id):
    conn = get_connection()
    if conn == None:
        return None
    try:
        id = (user_id["key"])
        print(id)
        sql = "SELECT device_name, model FROM Devices WHERE user_id=?"
        devices = conn.execute(sql, [id]).fetchall()
        return devices
    except:
        print ("Failed get devices")
    return None   

def edit_task():
    pass

def get_user_in_userlist(user):
    conn = get_connection()
    if conn == None:
        return None
    try:
        print(user)
        sql = "SELECT id FROM Users WHERE name=?"
        contacts = conn.execute(sql, [user]).fetchone()
        return contacts[0]
        
    except:
        print ("Failed to user in userlist")
    return None
