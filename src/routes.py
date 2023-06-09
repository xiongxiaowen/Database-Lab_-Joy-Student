"""
This module for handling routes
"""
from flask import render_template, request, redirect, session
from app import app
import users
import messages
import register_user_info
import like
import friend

@app.route("/")
def index():
    """
    This for homepage
    """
    list = messages.get_list()
    liked_messages = {}
    return render_template(
        "index.html",
        count=len(list),
        messages=list,
        liked_messages=liked_messages
        )


@app.route("/new")
def new():
    """
    This for new messages page.
    """
    return render_template("new.html")


@app.route("/send", methods=["POST"])
def send_message():
    """
    This for pushing new messages to forum
    """
    content = request.form["content"]
    if len(content) > 3000:
        return render_template("error.html", error="Viesti on liian pitkä")

    if messages.send(content):
        return redirect("/")

    return render_template("error.html", message="messages was not sent successfully")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This for login page.
    """
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")

    return render_template(
        "error.html",
        message="User not existing, or wrong username or password"
        )


@app.route("/logout")
def logout():
    """
    This for logout function.
    """
    users.logout()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    This for register page.
    """
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
            return render_template("error.html",
            message="Password field empty, please enter password"
            )
        # register the user
        if users.register(username, password1):
            return redirect("/fillup")
        else:
            return render_template("error.html", message="Registration not successful")


@app.route("/fillup", methods=["GET", "POST"])
def fillup():
    """
    This for filling the registration page.
    """
    if "user_id" in session:
        user_id = users.user_id()
        if request.method == "GET":
            return render_template("fillup.html")

        if request.method == "POST":
            name = request.form["name"]
            degree_program = request.form["degree_program"]
            faculty = request.form["faculty"]
            address = request.form["address"]
            if register_user_info.save_user_info(user_id, name, degree_program, faculty, address):
                return redirect("/registered")
            else:
                return render_template("error.html", message="Failed to save user information")
    else:
        return redirect("/login")


@app.route("/registered", methods=["GET"])
def registered():
    """
    This for displaying the registered info.
    """
    user_id = users.user_id()
    if "user_id" in session:
        user_info = register_user_info.get_user_by_id(user_id)
        username = session.get("username")
        friends = friend.get_friends(user_id)
        return render_template("registered.html",
        username=username,
        user=user_info,
        friends=friends)
    else:
        return render_template("error.html", message="User not found")


@app.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    """
    This for user account editing page.
    """
    if request.method == "GET":
        user = users.get_user_by_id(user_id)
        return render_template("edit.html", user=user)
    if request.method == "POST":
        users.check_csrf()
        username = request.form["username"]
        password = request.form["password"]
        users.update_user(user_id, username, password)
        return render_template("/updated.html", username=username, password=password)


@app.route("/update", methods=["GET", "POST"])
def update():
    """
    This for updating registered personal info.
    """
    user_id = users.user_id()
    if "user_id" in session:
        if request.method == "GET":
            user_info = register_user_info.get_user_by_id(user_id)
            return render_template("update.html", user_info=user_info)
        elif request.method == "POST":
            users.check_csrf()
            name = request.form["name"]
            degree_program = request.form["degree_program"]
            faculty = request.form["faculty"]
            address = request.form["address"]

            if register_user_info.update_user_info(user_id, name, degree_program, faculty, address):
                return redirect("/registered")
            else:
                return render_template("error.html", message="Failed to update user information")
    else:
        return render_template("error.html", message="User not found")


@app.route("/delete/<int:user_id>")
def delete(user_id):
    """
    This for removing personal info.
    """
    users.delete_user(user_id)
    return redirect("/registered")


@app.route("/like/<int:message_id>", methods=["POST"])
def like_message_route(message_id):
    """
    This for like operation.
    """
    if "like" in request.form:
        like.like_message(message_id)
    elif "unlike" in request.form:
        like.like_message(message_id)

    return redirect("/")

@app.route("/add_friend", methods=["POST"])
def add_friend():
    """
    This function handle adding friends.
    """
    user_id = users.user_id()
    friend_id = request.form["friend_id"]
    if not friend_id:
        # Handle the case when the friend ID is not provided
        return redirect("/registered")

    if not friend_id.isdigit():
        # Handle the case when the friend ID is not a valid integer
        return render_template("error.html",
        message="Invalid friend ID. Please enter a numeric value."
        )

    if "user_id" in session:
        friend_exists = users.get_user_by_id(friend_id)
        if friend_exists:
            friend.add_friend(user_id=user_id, friend_id=friend_id)
        else:
            return render_template("error.html",
            message="The specified friend ID does not exist."
            )
    else:
        return render_template("error.html", message="User not authenticated.")

    return redirect("/registered")
