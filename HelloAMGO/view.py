from flask import Flask, make_response,request, json,  render_template, redirect, g, Response, Request, session, flash
from HelloAMGO import *



@app.route("/view")
def view():
    return "helloworld"

@app.route("/")
def index_load():
    return render_template("index.html")

@app.route("/main")
def main_redirect():
    return redirect("/", code = 302) 

@app.route("/join")
def join():
    return render_template("join.html")

@app.route("/board1")
def board1():
    return render_template("board1.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")



@app.route('/signUp', methods=['POST'])
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


