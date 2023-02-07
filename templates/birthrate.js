import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sqlite3

connect = sqlite3.connect('births.db')
cursor = connect.cursor()
cursor.execute('SELECT * FROM birthstate6')

import pandas as pd
// Create your connection.
    cnx = sqlite3.connect('births.db')

df = pd.read_sql_query("SELECT * FROM birthstate6", cnx)


data = cursor.fetchall()
return render_template("index.html", data = data)