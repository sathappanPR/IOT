from flask import Flask,render_template
import pyrebase
from datetime import *

config = {
    "apiKey": "AIzaSyB5bJqmsRRqf5OQpTGBtNFFhcrjGBXTEb4",
    "authDomain": "smartparking-d872f.firebaseapp.com",
    "databaseURL": "https://smartparking-d872f-default-rtdb.firebaseio.com",
    "projectId": "smartparking-d872f",
    "storageBucket": "smartparking-d872f.appspot.com",
    "messagingSenderId": "256458912374",
    "appId": "1:256458912374:web:ec0eeeefdb3585cd8e6557",
    "measurementId": "G-8DGK77LQ22"
}



# def slot(x):
#     for i in range(len(x)):
#         return i

# def entry(entry):
#     for i in range(len(number_slots)):
#         entry = x.strftime("%Y-%m-%d, %H:%M %p")
#         return entry


# def exit(exit):
#     for i in range(len(number_slots)):
#         exit = x.strftime("%Y-%m-%d, %H:%M %p")
#         return exit

# def cost(cost):
#         for i in range(len(number_slots)):
#            tetime.strptime(entry, "%Y-%m-%d, %H:%M %p")
#             end_time = datetime.strptime(exit, "%Y-%m-%d, %H:%M %p")
#             delta = end_time - start_time
#             sec = delta.total_seconds()
#             min = sec / 60
#             hours = sec / (60 * 60)
#             print('difference in hours:', hours)

#             cost = hours*30
#             return str(cost)

# def checking(x):
#     val = list(x.values())
#     for i in range(len(val)):
#         if val[i]== 1:
#             return "Avaiable" 
#         else:
            # return "not Avaiable"

# todo = db.child("Parking/").get() 
# to = todo.val()
  

number_slots = [0,1]


firebase = pyrebase.initialize_app(config)
db = firebase.database()
todo = db.child("Parking/").get() 
to = todo.val()
print("realtime dir",todo)

app = Flask(__name__)

# x = datetime.now()
# entry = x.strftime("%Y-%m-%d, %H:%M %p")
# exit = x.strftime("%Y-%m-%d, %H:%M %p")


# exit = x.strftime("2023-01-09, 11:23 AM")

# entry_time = []
# exit_time = []

# val = list(to.values())

# for i in range(len(val)):
#     if val[i] == "Available":
#         exit_time.append(exit)
#         entry_time.append("New Entry")
 
#     elif val[i]== "Not Available":
#         entry_time.append(entry)
#         exit_time.append("New Entry")

        
#list(to.values())[0] , (slot(s),checking(to),entry,exit,cost(cost)) ,entry = entry,exit = exit,cost = cost(cost) ,"Entry","Exit","cost"
entry_time =  ["",""]
exit_time = ["",""]
cost = ["",""]

@app.route("/", methods=['GET','POST'])

def basic():
    global to,entry_time,exit_time,cost,delta,min
    headings = ("Slot number","avaiable","Entry","Exit")
    to_one = db.child("Parking/").get().val()
    # print("list to  : ",list(to.values()))
    # print("list to_one  : ",list(to_one.values()))
    # print(list(to_one.values())[1])
    for i in range(len(to_one.values())):
        # print("\nloop  : ",i)
        # print(list(to_one.values())[i], "/",list(to.values())[i]," == ",list(to_one.values())[i] != list(to.values())[i])
        if list(to_one.values())[i] != list(to.values())[i]:
            x = datetime.now()
            entry = x.strftime("%Y-%m-%d, %H:%M %p")
            exit = x.strftime("%Y-%m-%d, %H:%M %p")

            if list(to_one.values())[i] == "Available":
                exit_time[i] = exit
                # print("---------------------------\n")
                # print("exit time :  ",exit_time[i])
                # print("entry time : ",entry_time[i])
                # print("---------------------------")
                entry_time[i] = "New Entry"
                # cost[i] = "New entry"

                # delta[i] = entry_time[i] - exit_time[i]
                # print("delta(i) : ",delta[i])
                # sec = delta[i].total_seconds()
                # print(sec)
                # min = sec / 60
                # hours = sec / (60 * 60)
                # cost[i] = hours*30
                # print("Cost of i : ",cost[i])
        
            elif list(to_one.values())[i] == "Not Available": 
                entry_time[i] = entry 
                exit_time[i] = "New Entry"
                # print("---------------------------\n")
                # print("exit time :  ",exit_time[i])
                # print("entry time : ",entry_time[i])
                # print("---------------------------\n")
                # cost[i] = "New entry"
        
    to = to_one
    print(" to  : ",list(to.values()))
    print(" to_one  : ",list(to_one.values()))
    return render_template("Welcome.html",headings=headings,len = len(number_slots), check = list(to_one.values()),Entry = entry_time,Exit = exit_time)
    

if __name__ == "__main__":
    app.run(debug=True)


 


# dd/mm/YY H:M:S

