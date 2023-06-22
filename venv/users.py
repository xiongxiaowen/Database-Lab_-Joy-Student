import os
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text


def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)
    

def user_id():
    return session.get("user_id", 0)


#function to fetch the user by ID
def get_user_by_id(user_id):
    sql = text("SELECT * FROM users WHERE id=:user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    user = result.fetchone()
    return user

def update_user(user_id, username, password):
    hash_value = generate_password_hash(password)
    sql = text("UPDATE users SET username=:username, password=:password WHERE id=:user_id")
    db.session.execute(sql, {"username": username, "password": hash_value, "user_id": user_id})
    db.session.commit()

def delete_user(user_id):
    sql = text("DELETE FROM users WHERE id=:user_id")
    db.session.execute(sql, {"user_id": user_id})
    db.session.commit()

"""
def add_friend(user_id, friend_id):
    sql = text("INSERT INTO friends (user_id, friend_id) VALUES (:user_id, :friend_id)")
    db.session.execute(sql, {"user_id": user_id, "friend_id": friend_id})
    db.session.commit()

def get_friends(user_id):
    sql = text("SELECT users.id, users.username FROM users JOIN friends ON users.id = friends.friend_id WHERE friends.user_id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    friends = result.fetchall()
    return friends
"""
