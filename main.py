from flask import Blueprint,render_template_string

main=Blueprint("main",__name__)

@main.route("/")
def index():
 return "Hello world"

@main.route("/profile")
def profile():
 return "Profile here!"