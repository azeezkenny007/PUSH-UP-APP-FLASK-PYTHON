from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "Login Page"


@auth.route("/signup")
def signup():
    return "This page would be used to signup users!"


@auth.route("/logout")
def logout():
    return "Use thsi view to logout"
