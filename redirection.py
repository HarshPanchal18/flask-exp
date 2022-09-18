#!/usr/bin/env python

from flask import Flask
app=Flask(__name__)

#------------------------------------------
def about():
    return "About Page"

# add_url_route(<url rule>, <endpoint>, <view function>)
# This function is mainly used in the case if the view function is not given and we need to connect a view function to an endpoint externally by using this function.
app.add_url_rule("/about","about",about)

# -----------------------------------------

#The url_for() function is used to build a URL to the specific function dynamically. The first argument is the name of the specified function, and then we can pass any number of keyword argument corresponding to the variable part of the URL.

#This function is useful in the sense that we can avoid hard-coding the URLs into the templates by dynamically building them using this function.

@app.route('/admin')
def admin():
    return 'admin'

@app.route('/staff')
def staff():
    return 'staff'

@app.route('/student')
def student():
    return 'student'

@app.route("/user/<name>")
def user(name):
    if name=='admin':
        return redirect(url_for('admin'))

    if name=='staff':
        return redirect(url_for('staff'))

    if name=='student':
        return redirect(url_for('student'))


app.run(debug=True)
