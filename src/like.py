"""
This module for like functions 
"""
from sqlalchemy import text
from db import db
import users


def like_message(message_id):
    """
    allow to like message. 
    """
    user_id = users.user_id()
    # User is not logged in, cannot like message
    if user_id == 0:
        return False

    sql = text("SELECT id FROM likes WHERE user_id = :user_id AND post_id = :message_id")
    result = db.session.execute(sql, {"user_id": user_id, "message_id": message_id})
    existing_like = result.fetchone()

    if existing_like:
        # User has already liked the message, so remove the like
        sql = text("DELETE FROM likes WHERE id = :like_id")
        db.session.execute(sql, {"like_id": existing_like.id})
        db.session.commit()
        return False  # Unliked the message
    else:
        # User has not liked the message, so add a new like
        sql = text("INSERT INTO likes (user_id, post_id) VALUES (:user_id, :message_id)")
        db.session.execute(sql, {"user_id": user_id, "message_id": message_id})
        db.session.commit()
        return True
