from flask import Flask, make_response, render_template, redirect, g

app = Flask(__name__)

@app.before_request()

@app.route("/")
def index_load():
    return render_template("index.html")

@app.route("/main")
def main_redirect():
    return redirect("/", code = 302)

if __name__ == "__main__":
    app.debug = True
    app.run()