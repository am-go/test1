from flask import Flask, make_response,request, json,  render_template, redirect, g, Response, Request, session, flash
from HelloAMGO import application



@application.route("/view")
def view():
    return "helloworld"

@application.route("/")
def index_load():
    return render_template("index.html")

@application.route("/main")
def main_redirect():
    return redirect("/", code = 302) 


@application.route("/board1")
def board1():
    return render_template("board1.html")


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


