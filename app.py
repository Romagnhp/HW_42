from flask import Flask, render_template
import datetime

obj_Flask = Flask(__name__)

myDictionary = {'name':'Honcharov Roman', 'phoneNumber':'099-248-47-98', 'mail':'romagnhp@gmail.com'}

def myStyle():
    t = datetime.datetime.now().hour
    if 6 <= t < 17:
        return 'css/styleWhite.css'
    else:
        return 'css/styleBlack.css'

@obj_Flask.route("/")
def lounch_Rezume():
    #return render_template("/index.html", name = 'Honcharov Roman', phoneNumber = '099-248-47-98', mail= 'romagnhp@gmail.com')
    return render_template("/index.html", **myDictionary, cssPath = myStyle())

obj_Flask.run(debug=True) 