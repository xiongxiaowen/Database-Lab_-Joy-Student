from db import db
import users
from sqlalchemy import text


def save_user_info(user_id, name, degree_program, faculty, address):
    try:
        sql = text("INSERT INTO usersinfo (user_id, users_name, degree_program, faculty, address)"
                   "VALUES (:user_id, :name, :degree_program, :faculty, :address)")
        db.session.execute(sql, {"user_id": user_id, "name": name, "degree_program": degree_program, "faculty": faculty, "address": address})
        db.session.commit()
    except:
        return False
    return True

def get_user_by_id(user_id):
    sql = text("SELECT * FROM usersinfo WHERE user_id = :user_id")
    result = db.session.execute(sql, {"user_id": user_id})
    user_info = result.fetchone()
    return user_info


def update_user_info(user_id, name, degree_program, faculty, address):
    try:
        sql = text("UPDATE usersinfo SET users_name=:name, degree_program=:degree_program, faculty=:faculty, address=:address WHERE user_id=:user_id")
        db.session.execute(sql, {"name": name, "degree_program": degree_program, "faculty": faculty, "address": address, "user_id": user_id})
        db.session.commit()
    except:
        return False
    return True