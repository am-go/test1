from HelloAMGO.app.dbModule import *
from flask import request, redirect, url_for
from HelloAMGO import application

conn = Database()

@application.route("/board/answerlist", methods=["POST"])
def connect():
    print("들어왔어요")
    "db접속"
    "select"
    "response 객체 담아서"
    "return "
    "redirect"
    "url_for"
    "  "
