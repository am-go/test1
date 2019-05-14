from flask import Flask, make_response,request, json,  render_template, redirect, g, Response, Request, session, flash
from HelloAMGO.__init__ import *
from datetime import timedelta

app.config.update(
	SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(minutes=31)      # 31 days  cf. minutes=30
)

@app.before_first_request
def before_request():
    if session.get('logged_in') != True:
        return redirect('/login')
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login/access', methods = ['POST'])
def loginAccess():
    _ID = request.form.get('inputID')
    _password = request.form.get('inputPassword')
    if _ID == 'id' and _password == 'pw':
        session['logged_in'] = True  # 세선 해제는 어떻게?
        print(session.get('logged_in'))
        return redirect('/')
    else:
        flash('유저네임이나 암호가 맞지 않습니다.')
        return redirect('/login')

@app.route('/logout')
def logout():
    if session.get('logged_in') != True:
        return redirect('/login')
    elif session.get('logged_in') == True:
        del session['logged_in']
        return redirect('/login')