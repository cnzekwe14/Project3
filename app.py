import sqlite3
from flask import Flask, render_template

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def part1():
    return render_template("index.html")

@app.route('/births')
def part2():
    conn = sqlite3.connect("births.db")
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cursor = cur.execute('SELECT DISTINCT YEAR FROM birthstate6')
    items = cursor.fetchall()
    
        
    return render_template("index.html",items=items)
  
    
# conn1 = sqlite3.connect("birth_rate.db")
# cur1 = conn.cursor()
# cursor1 = cur.execute('SELECT * FROM birth_data2')
# items1 = cursor.fetchall()
# return render_template("births.html",items=items)

    
    

if __name__ == '__main__':
    app.run(debug = True)