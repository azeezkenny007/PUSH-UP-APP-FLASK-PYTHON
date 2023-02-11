from flask import Blueprint, render_template_string,render_template,redirect,url_for,request,flash
from flask_login import login_user,logout_user,login_required,current_user
from .models import Workout,User,session


main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html",name=current_user.name)


@main.route("/new")
@login_required
def new_workout():
    return render_template("create_workout.html")

@main.route("/new",methods=["POST"])
@login_required
def new_workout_post():
    pushups= request.form.get("pushups")
    comment = request.form.get("comment")
    workout = Workout(pushups=pushups,comment=comment,author=current_user)
    session.add(workout)
    session.commit()
    flash("workout has been added!")
    return redirect(url_for("main.user_workouts"))


@main.route("/all")
@login_required
def user_workouts():
    user = session.query(User).filter_by(email=current_user.email).first()
    workout =user.workout
    return render_template("all_workouts.html",user=user,workouts=workout)
    