from db import db
import users
from sqlalchemy import text


def save_user_info(user_id, name):
    try:
        sql = text("INSERT INTO usersinfo (user_id, users_name) "
                   "VALUES (:user_id, :name)")
        db.session.execute(sql, {"user_id": user_id, "name": name})
        db.session.commit()
    except:
        return False
    return True

def get_user_by_id(user_id):
    sql = text("SELECT * FROM usersinfo WHERE user_id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    user_info = result.fetchone()
    return user_info