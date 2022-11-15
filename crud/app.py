from flask import Flask,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tables'

mysql=MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/editForm')
def editForm():
    args=request.args
    id=args.get("id")
    cursor=mysql.connection.cursor()
    cursor.execute('''select * from users where userid=%s''',(id))
    data=cursor.fetchall()
    return render_template('editForm.html',data=data)

@app.route('/editUser',methods=['POST','GET'])
def edituser():
    id=request.form['id']
    password=request.form['password']
    username=request.form['userName']
    cursor=mysql.connection.cursor()
    cursor.execute('''update users set username=%s, password=%s where userid=%s''',(username,password,id))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('list'))

@app.route('/signup',methods=['POST','GET'])
def login():
    if request.method== "GET":
        return "Sign up via signup form"

    if request.method=="POST":
        username=request.form['userName']
        password=request.form['password']
        cursor=mysql.connection.cursor()
        cursor.execute('''insert into users(username,password) values(%s,%s)''',(username,password))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

@app.route('/delete')
def delete():
    args=request.args
    id=args.get("id")
    cursor=mysql.connection.cursor()
    cursor.execute("delete from users where userid= %s",(id))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('list'))

@app.route('/list')
def list():
    cursor = mysql.connection.cursor()
    cursor.execute('''SELECT * FROM users''')
    data = cursor.fetchall()
    return render_template('list.html', data=data)

@app.route('/logout')
def logout():
    return redirect(url_for('form'))

app.run(debug=True)
