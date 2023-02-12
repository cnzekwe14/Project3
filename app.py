import sqlite3
import pandas as pd
from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def part1():
    return render_template("index.html")

@app.route('/births')
def part2():
    conn = sqlite3.connect("births.db")
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cursor = cur.execute('SELECT DISTINCT YEAR FROM birthstate6 WHERE YEAR NOT 2005')
    years1 = cursor.fetchall()
    cursor1 = cur.execute('SELECT ROUND(AVG(FERTILITY_RATE),1) FROM birthstate6 GROUP BY YEAR ORDER BY YEAR DESC')
    fertility1 = cursor1.fetchall()
    
    # textuserstate = getRequestString('UserS')
    cursor2 = cur.execute('SELECT STATE FROM birthstate6')
    state1 = cursor2.fetchall()
    df = pd.DataFrame({
        'x': years1,
        'y': fertility1
        # 'z': state1
    })
    
    chart_data = df.to_dict(orient='records')
     
    return jsonify(chart_data)
  
    
# conn1 = sqlite3.connect("birth_rate.db")
# cur1 = conn.cursor()
# cursor1 = cur.execute('SELECT * FROM birth_data2')
# items1 = cursor.fetchall()
# return render_template("births.html",items=items)

    
    

if __name__ == '__main__':
    app.run(debug = True)