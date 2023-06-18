from app import app
from flask import render_template, request, redirect
import users, messages

@app.route("/")
def index():
    list = messages.get_list()
    return render_template("index.html", count=len(list), messages=list)


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/send", methods=["POST"])
def send_message():
    content = request.form["content"]
    if messages.send(content):
        return redirect("/")
    else:
        return render_template("error.html", message="messages was not sent successfully")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="User not existing, or wrong username or password")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Username must be 1-20 characters long")
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        # validate inputs
        if password1 != password2:
            return render_template("error.html", message="Two passwords are different!")
        if password1 == "":
            return render_template("error.html", message="Password field empty, please enter password")
        # register the user
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration not successful")


@app.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    if request.method == "GET":
        user = users.get_user_by_id(user_id)
        return render_template("edit.html", user=user)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users.update_user(user_id, username, password)
        return redirect("/")


@app.route("/delete/<int:user_id>")
def delete(user_id):
    users.delete_user(user_id)
    return redirect("/")

