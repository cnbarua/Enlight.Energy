from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import config
import hashlib

app = Flask(__name__)

app.config['SECRET_KEY'] = config.HEX_SEC_KEY
app.config['MYSQL_HOST'] = config.MYSQL_HOST
app.config['MYSQL_USER'] = config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = config.MYSQL_DB
app.config['MYSQL_PORT'] = config.MYSQL_PORT

mysql = MySQL(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    passw = hashlib.md5(request.form['pass'].encode()).hexdigest()

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, passw))
    user = cur.fetchone();
    cur.close()

    if user is not None:
        session['email'] = email
        session['name'] = user[1]
        session['surname'] = user[2]

        return redirect(url_for('tasks'))
    else:
        return render_template('index.html', message = 'Incorrect User o Password')

@app.route("/tasks", methods=['GET'])
def tasks():
    return render_template('tasks.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/new-task', methods=['POST'])
def newTask():
    title = request.form['title']
    descri = request.form['description']
    

if __name__ == '__main__':
    app.run(debug=True)

