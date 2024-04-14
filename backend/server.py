from flask import Flask,jsonify,request,send_file
from data.connector import create_tables,new_user,new_device,new_task,get_tasks,edit_task,get_user_in_userlist,get_devices

app = Flask(__name__)

create_tables()

@app.route("/")
#@app.route("/index")
#def index():
#    return send_file("public//index.html")


@app.route("/api/users",methods=["GET","POST"])
def fetch_users():
    if request.method == "GET":
        data = request.json
        temp_name = (data["name"])
        temp_user = get_user_in_userlist(temp_name)
        if temp_user == None:
            return "Internal Server Error",500
        return jsonify(temp_user)
    else:
        data = request.json
        temp_name = (data["name"])
        temp_user = get_user_in_userlist(temp_name)
        if temp_user == None:
            success = new_user(temp_name)
            if success == None:
                return "Internal Server Error",500
            return "Success",201
        return "Conflict",409
        

@app.route("/api/devices",methods=["GET","POST"])
def fetch_devices():
    if request.method == "GET":
        data = request.json
        temp_devices = get_devices(data)
        devices = []
        for i in range(len(temp_devices)):
            devices.append({"name":temp_devices[i][0],"model":temp_devices[i][1]})
        return jsonify(devices)
    else:
        data = request.json
        print (data)
        success = new_device(data)
        if success == None:
            return "Internal Server Error",500
        return "Success",201

@app.route("/api/todos",methods=["GET","POST"])
def fetch_todos():
    if request.method == "GET":
        data = request.json
        print (data)
        temp_todos = get_tasks(data)
        todos = []
        for i in range(len(temp_todos)):
            todos.append({"name":temp_todos[i][0],"deadline":temp_todos[i][1],"device":temp_todos[i][6],"device_model":temp_todos[i][7]})
        return jsonify(todos)
    else:
        data = request.json
        print (data)
        success = new_task(data)
        if success == None:
            return "Internal Server Error",500
        return "Success",201
    
    
app.run("127.0.0.1",port=3000)

