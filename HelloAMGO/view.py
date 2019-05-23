from HelloAMGO import application
from flask import json, make_response, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from HelloAMGO.app.dbModule import *


@application.route("/")
def index_load():
    return render_template("indexsample.html")

@application.route("/main")
def main_redirect():
    return redirect("/", code = 302)


@application.route('/signup')
def signup():
    return render_template("signup.html")



@application.route('/signUp', methods=['POST'])
def signUp():

    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    #validating
    if _name and _email and _password:
        result = "ALL GOOD"
        res = make_response(render_template('signup.html', resul = result))
        return res
    else:
        result = "BAD"
        res = make_response(render_template('signup.html', resul=result))
        return res


