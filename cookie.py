#!/usr/bin/env python

from flask import *
app=Flask(__name__)

@app.route("/cookie")
def cook():
    ans=make_response("<h2> Cookie is set </h2>")
    ans.set_cookie('Harsh','India')
    return ans

app.run(debug=True)
