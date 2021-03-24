from flask import Flask,Blueprint,render_template, url_for, request, redirect, flash
from . import db
from flask_login import login_user,logout_user,login_required
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    render_template("login.html")

@auth.route("/login", methods=["POST"])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password,password):
        flash('Please check your login details')
        return redirect(url_for('main.login'))

    return redirect(url_for("main.home"))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))