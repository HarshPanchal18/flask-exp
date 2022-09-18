#!/usr/bin/env python

from flask import *

app=Flask(__name__)

@app.route("/login",methods=['POST'])
def login():
    uname=request.form['uname']
    passw=request.form['pass']

    if uname=='harsh' and passw=='harsh':
        return "Welcome %s " %uname
    else
        return 'Invalid Credentials!'

app.run(debug=True)
# Run this script and go to the browser with login.html
