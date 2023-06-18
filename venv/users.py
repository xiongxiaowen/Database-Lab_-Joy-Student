import os
from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import text

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
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
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)
    

def user_id():
    return session.get("user_id", 0)

def get_all_users():
    #executes a SQL query to fetch the users' data from the "users" table in the database. 
    sql = "SELECT * FROM users"
    result = db.session.execute(text(sql))
    users = result.fetchall()
    return users

def get_user_by_id(user_id):
    sql = "SELECT * FROM users WHERE id=:user_id"
    result = db.session.execute(text(sql), {"user_id": user_id})
    user = result.fetchone()
    return user

def update_user(user_id, username, password):
    hash_value = generate_password_hash(password)
    sql = "UPDATE users SET username=:username, password=:password WHERE id=:user_id"
    db.session.execute(text(sql), {"username": username, "password": hash_value, "user_id": user_id})
    db.session.commit()

def delete_user(user_id):
    sql = "DELETE FROM users WHERE id=:user_id"
    db.session.execute(text(sql), {"user_id": user_id})
    db.session.commit()