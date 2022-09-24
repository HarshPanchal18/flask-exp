#!/usr/bin/env python

from flask import *
app=Flask(__name__)

@app.route('/')
def upload():
    return render_template("fileUploadForm.html")

@app.route('/success',methods=['post'])
def success():
    if request.method=='post':
        fl=request.files['file']
        fl.save(fl.filename)
        return render_template("success2.html",name=fl.filename)

app.run(debug=True)
