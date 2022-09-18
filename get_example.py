#!/usr/bin/env python

from flask import *

app=Flask(__name__)

@app.route("/login",methods=['GET'])
def login():
    uname=request.args.get('uname')
    # Here, the args is a dictionary object which contains the list of pairs of form parameter and its corresponding value.
    passw=request.args.get('pass')

    if uname=='harsh' and passw=='harsh':
        return "Welcome %s ! " %uname
    else
        return 'Invalid Credentials!'

app.run(debug=True)
# Run this script and go to the browser with login.html
