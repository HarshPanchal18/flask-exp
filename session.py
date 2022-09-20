#!/usr/bin/env python

from flask import *
app=Flask(__name__)
app.secret_key="harsh"

@app.route("/")
def home():
    res=make_response("<h3>Session variable is set, <a href='/get'>GET VARIABLE</a></h3>")
    session['response']='I am ready for upcoming session...'
    return res

@app.route("/get")
def getVar():
    if 'response' in session:
        x=session['response']
        return render_template('getsession.html',name=x)

app.run(debug=True)
