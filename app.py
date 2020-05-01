from flask import Flask, session, redirect, url_for, request, render_template
from markupsafe import escape
import secrets

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(16)

@app.route('/')
def index():
    if 'username' in session:
        return render_template("home.html")
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        """This is where user creation and DB dump occurs"""
        "if everything is right"
        return render_template("login.html")
    return render_template("signup.html")

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'), 404