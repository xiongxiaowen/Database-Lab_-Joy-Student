"""
This module for users operations.
"""
import secrets
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session, abort, request
from db import db


def login(username, password):
    """
    This for login function.
    """
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def logout():
    """
    This for logout function.
    """
    del session["user_id"]

def register(username, password):
    """
    This  for register function.
    """
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)


def user_id():
    """
    This for defining user_id.
    """
    return session.get("user_id", 0)


def get_user_by_id(user_id):
    """
    This for obtain data based on user id, function to fetch the user by ID
    """
    sql = text("SELECT * FROM users WHERE id=:user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    user_info = result.fetchone()
    return user_info

def update_user(user_id, username, password):
    """
    This for updating user info to database.
    """
    hash_value = generate_password_hash(password)
    sql = text("UPDATE users SET username=:username, password=:password WHERE id=:user_id")
    db.session.execute(sql, {"username": username, "password": hash_value, "user_id": user_id})
    db.session.commit()

def delete_user(user_id):
    """
    This for deleting user info from database.
    """
    sql = text("UPDATE usersinfo SET degree_program = NULL, faculty = NULL, address = NULL WHERE user_id = :user_id")
    db.session.execute(sql, {"user_id": user_id})
    db.session.commit()

def check_csrf():
    """
    This for csrf checking.
    """
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
