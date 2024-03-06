from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '39bb37cf36d3b29a9280d8a70a0eed42'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    passw = request.form['pass']

    if email == 'cbarua@hotmail.com' and passw == "Asdf1234":
        session['email'] = email
        session['name'] = 'Claudio'
        session['surname'] = 'Barua'

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

if __name__ == '__main__':
    app.run(debug=True)

