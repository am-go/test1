from flask import Flask, make_response,request,url_for,\
    json,  render_template, redirect, g, Response, Request, session, flash
from HelloAMGO import application
from datetime import timedelta
from flask_bcrypt import Bcrypt
from HelloAMGO.app.dbModule import *

application.config.update(
	SECRET_KEY="secretkey",
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(minutes=31),      # 31 days  cf. minutes=30
    BCRYPT_LEVEL = 10
)

exceptionList = ['/login', '/join', '/login/access', '/join/confirm']
@application.before_request
def before_request():
    if (not 'logged_in' in session) and not(request.path in exceptionList):
        if request.path == '/join':
            return redirect(url_for('join'))
        else:
            return redirect(url_for('login'))


@application.route('/login')
def login():
    return render_template("login.html")

@application.route('/login/access', methods = ['POST'])
def loginAccess():
    _ID = request.form.get('inputID')
    _password = request.form.get('inputPassword')
    #해쉬 객체 생성
    conn = Database()
    bcrypt = Bcrypt(application)
    getPw = conn.executeOne(("SELECT pw FROM users WHERE id='"+_ID+"'"))
    is_same = bcrypt.check_password_hash(bytes(getPw['pw'], 'utf8'), _password)  # True

    if is_same:
        print("세션 생성 성공")

        session['logged_in'] = _ID
        return redirect(url_for('helloworld'))
    else:
        return redirect(url_for('login'))


@application.route('/logout')
def logout():
    if session.get('logged_in') != True:
        return redirect(url_for('index_load'))
    elif session.get('logged_in') == True:
        del session['logged_in']
        return redirect(url_for('login'))