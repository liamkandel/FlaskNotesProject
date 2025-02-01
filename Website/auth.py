from flask import Blueprint, flash
from flask import render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing")

@auth.route("/logout")
def logout():
    return render_template("home.html")

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print('test')
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('passwordOne')
        confirmPassword = request.form.get('passwordTwo')

        if len(email) < 4:
            flash("Email must be at least 5 characters.", category="error")
        if len(firstName) < 2:
            flash("First name must be at least 3 characters", category="error")
        if password != confirmPassword:
            flash("Passwords do not match.", category="error")
        if len(password) < 7:
            flash("Password is too short.", category="error")
        else:
            flash("Account created!", category="success")
            
    return render_template("signup.html")