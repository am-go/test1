from HelloAMGO import application
from flask import render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from HelloAMGO.app.dbModule import *

@application.route("/join")
def join():
    return render_template("join.html")

@application.route("/join/confirm", methods=['POST'])
def join_confirm():
    _id = request.form.get("inputID")
    _name = request.form.get("inputName")
    _email = request.form.get("inputEmail")
    _password = request.form.get("inputPassword")
    _phoneNum = request.form.get("inputMobile")
    _school = request.form.get("inputSchool")

    try:
        conn = Database()
        bcrypt = Bcrypt(application)
        pw_hash = bcrypt.generate_password_hash(_password)

        pw_hash = pw_hash.decode()
        sql = "INSERT INTO users(id, name, email, pw, phoneNum, school) VALUES(\"%s\",\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" \
                  %(_id, _name, _email, pw_hash, _phoneNum, _school)
        print(sql)
        conn.execute(sql)
        conn.commit()
        return redirect(url_for('index_load'))
    except Exception as ex:  # 에러 종류
        print('에러가 발생 했습니다', ex)
        return redirect(url_for('login'))
