""""Flask App"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    """Home Screen"""
    return "This is Michael McSorley CPS3500 Midterm Project!"


@app.route("/add/<username>")
def add(username):
    """Username addition"""
    return render_template('user.html', username=username)

if __name__ == "__main__":
    app.run()
