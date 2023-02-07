from flask import Flask, render_template
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3

app = Flask(__name__, template_folder = "templates")

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
#     connect = sqlite3.connect('births.db')
#     cursor = connect.cursor()
#     cursor.execute('SELECT * FROM birthstate6')
    
#     import pandas as pd
# # Create your connection.
#     cnx = sqlite3.connect('births.db')

#     df = pd.read_sql_query("SELECT * FROM birthstate6", cnx)
#     df
    

    # return render_template("index.html")

    with sqlite3.connect("births.db") as users:
                cursor = users.cursor()
                cursor.execute("SELECT * FROM birthstate6")
                users.commit()
                
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    
      
