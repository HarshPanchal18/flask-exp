#!/usr/bin/env python

from flask import *

app=Flask(__name__)

@app.route('/', methods=['POST'])
def login():
    n1=str(request.form['num1'])
    n2=str(request.form['num2'])
    return str(int(n1)+int(n2))


'''
@app.route('/', methods=['GET'])
def loginget():
    n1=str(request.form['num1'])
    args = request.args
    return args
    n2=str(request.form['num2'])

    return args.get("num1", default=0, type=int)
    return args.get("num2", default=0, type=int)

    return str(int(n1)+int(n2))
'''

'''@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      n1 = request.form['num1']
      n2 = request.form['num1']
      return redirect(url_for('success',num1=n1,num2=n2))
   else:
      n1 = request.args.get('num1')
      n2 = request.args.get('num1')
      return redirect(url_for('success',num1=n1,num2=n2))
'''

@app.route('/')
def my_form():
    return render_template("login.html")

app.run(debug=True)
