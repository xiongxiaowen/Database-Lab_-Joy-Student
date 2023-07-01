"""
This module for message functions 
"""
from sqlalchemy import text
from db import db
import users



def get_list():
    """
    display messages to the list on the homepage, as a public forum. 
    """
    sql = text("SELECT M.id, M.content, U.username, M.sent_at, COUNT(L.id) AS like_count "
               "FROM messages M "
               "JOIN users U ON M.user_id = U.id "
               "LEFT JOIN likes L ON M.id = L.post_id "
               "GROUP BY M.id, M.content, U.username, M.sent_at "
               "ORDER BY M.id")
    result = db.session.execute(sql)
    return result.fetchall()


def send(content):
    """
    send user's message content to the homepage, the public forum. 
    """
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = text("INSERT INTO messages (content, user_id, sent_at) VALUES (:content, :user_id, NOW())")
    db.session.execute(sql, {"content":content, "user_id":user_id})
    db.session.commit()
    return True

