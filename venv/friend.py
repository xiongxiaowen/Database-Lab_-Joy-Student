"""
This module for adding friends functions 
"""
from sqlalchemy import text
from db import db



def add_friend(user_id, friend_id):
    """
    adding friends functions, check if the friendship already exists
    """
    sql = text("SELECT user_id FROM friends WHERE user_id = :user_id AND friend_id = :friend_id")
    result = db.session.execute(sql, {"user_id": user_id, "friend_id": friend_id})
    existing_friendship = result.fetchone()

    if existing_friendship:
        # Friendship already exists, no need to add again
        return False
    else:
        # Add the friendship
        sql = text("INSERT INTO friends (user_id, friend_id) VALUES (:user_id, :friend_id)")
        db.session.execute(sql, {"user_id": user_id, "friend_id": friend_id})
        db.session.commit()
        return True


def get_friends(user_id):
    """
    fetch friends.
    """
    sql = text("SELECT usersinfo.user_id, usersinfo.users_name FROM usersinfo JOIN friends ON usersinfo.id = friends.friend_id WHERE friends.user_id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    friends = result.fetchall()
    return friends

