#!/usr/bin/env python

from flask import Flask,render_template,request

app=Flask(__name__,template_folder='templates')

@app.route('/')
def helloWorld():
    return "Hello World"

@app.route('/table/<int:no>/')
def tableNum(no):
    return render_template("index.html",n=no)

app.run(debug=True)
