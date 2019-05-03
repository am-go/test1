from flask import Flask, make_response, render_template, redirect, g, Response, Request
from HelloAMGO import app

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
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("index.html")
