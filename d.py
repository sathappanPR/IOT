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

number_slots = [0,1]

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

x = datetime.now()
entry = x.strftime("%Y-%m-%d, %H:%M %p")
exit = x.strftime("2023-01-09, 11:23 AM")

def slot(x):
    for i in range(len(x)):
        return i


todo = db.child("Parking/").get()
to = todo.val()

def entry(entry):
    for i in range(len(number_slots)):
        entry = x.strftime("%Y-%m-%d, %H:%M %p")
        return entry


def exit(exit):
    for i in range(len(number_slots)):
        exit = x.strftime("%Y-%m-%d, %H:%M %p")
        return exit

def cost(cost):
        for i in range(len(number_slots)):
            start_time = datetime.strptime(entry, "%Y-%m-%d, %H:%M %p")
            end_time = datetime.strptime(exit, "%Y-%m-%d, %H:%M %p")
            delta = end_time - start_time
            sec = delta.total_seconds()
            min = sec / 60
            hours = sec / (60 * 60)
            print('difference in hours:', hours)

            cost = hours*30
            return str(cost)

def checking(x):
    val = list(x.values())
    for i in range(len(val)):
        if val[i]== 1:
            return "Avaiable" 
        else:
            return "not Avaiable"

# todo = db.child("Parking/").get() 
# to = todo.val()
# checking(to)    

lena = ["s","s"]
parking = [0,1]
        
#list(to.values())[0] , (slot(s),checking(to),entry,exit,cost(cost)) ,entry = entry,exit = exit,cost = cost(cost) ,"Entry","Exit","cost"

@app.route("/", methods=['GET','POST'])

def basic():
    # todo = db.child("Parking/").get()
    # to = todo.val()
    headings = ("Slot number","avaiable")
    return render_template("Welcome.html",headings=headings,len = len(number_slots),check = list(to.values()))
    

if __name__ == "__main__":
    app.run(debug=True)


 


# dd/mm/YY H:M:S

