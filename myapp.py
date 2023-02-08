from flask import Flask, render_template, request
import sqlite3
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def states():
    year = request.form["YEAR"]
    state = request.form["STATE"]
    births = request.form["BIRTHS"]
    connection = sqlite3.connect(currentdirectory + "/births.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO Births VALUE ({y},{st},{bir})".format(y = year, st = state, bir = births)
    cursor.execute(query1)
    connection.commit()

@app.route("/resultpage", methods = ["GET"])
def resultpage():
    try:
        if request.method == "GET":
            state = requests.args.get(State)
            connection = sqlite3.connect(currentdirectory + "/births.db")
            cursor = connection.cursor()
            query1 = "SELECT * FROM Birthstate"
            result = cursor.execute(query1)
            result = result.fetchall()
            return render_template("index.html")

    except:
        return render_template("index.html")
if __name__ =="__main__":
    app.run()

