from HelloAMGO import application
from flask import json, make_response, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from HelloAMGO.app.dbModule import *

@application.route("/board")
def board():
    lst = []
    conn = Database()
    sql = "SELECT name FROM univs"
    univNames = conn.executeAll(sql)
    for i in range(len(univNames)):
        lst.append(univNames[i]['name'])

    return render_template("board.html", lst=lst)

@application.route("/board/board-list/<test_univ>")
def board_list(test_univ):
    lst = ["2018","2017","2016","2015","2014"]
    print(test_univ)
    return render_template("board-list.html", lst=lst)

@application.route("/board-answer")
def board_answer():
    return render_template("board-answer.html")

@application.route("/answerlist")
def answerlist():
    return render_template("answerlist.html")