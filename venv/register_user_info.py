from db import db
import users
from sqlalchemy import text


def save_user_info(user_id, name, gender, faculty, student_number, address):
    try:
        sql = text("INSERT INTO usersinfo (user_id, users_name, gender, faculty, student_number, address_user) "
                   "VALUES (:user_id, :name, :gender, :faculty, :student_number, :address)")
        db.session.execute(sql, {"user_id": user_id, "name": name, "gender": gender, "faculty": faculty,
                                 "student_number": student_number, "address": address})
        db.session.commit()
    except:
        return False
    return True