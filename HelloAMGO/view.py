from HelloAMGO import application
from flask import json, make_response, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from HelloAMGO.app.dbModule import *


@application.route("/view")
def view():
    return "helloworld"

@application.route("/")
def helloworld():
    return render_template("indexsample.html")

@application.route("/main")
def main_redirect():
    return redirect("/", code = 302) 


@application.route("/board")
def board():
    lst = ["서울대","고려대","연세대","한국외대","서강대"]
    return render_template("board.html", lst=lst)

@application.route("/board-list")
def board_list():
    lst = ["2018","2017","2016","2015","2014"]
    return render_template("board-list.html", lst=lst)

@application.route("/board-answer")
def board_answer():
    return render_template("board-answer.html")

@application.route("/answerlist")
def answerlist():
    return render_template("answerlist.html")

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


