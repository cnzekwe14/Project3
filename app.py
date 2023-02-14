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
    cursor = cur.execute('SELECT DISTINCT YEAR FROM birthstate6 WHERE YEAR != 2005')
    years1 = cursor.fetchall()
    cursor1 = cur.execute('SELECT ROUND(AVG(FERTILITY_RATE),1) FROM birthstate6 WHERE YEAR != 2005 GROUP BY YEAR ORDER BY YEAR DESC')
    fertility1 = cursor1.fetchall()
    
    cursor2 = cur.execute('SELECT STATE FROM birthstate6')
    state1 = cursor2.fetchall()
    df = pd.DataFrame({
        'x': years1,
        'y': fertility1
        # 'z': state1
    })
    
    chart_data = df.to_dict(orient='records')
     
    return jsonify(chart_data)

@app.route('/birth_rate')
def part3():
    conn1 = sqlite3.connect("birth_rate.db")
    cur1 = conn1.cursor()
    cursor1 = cur1.execute('SELECT YEAR FROM birth_data2')
    years2 = cursor1.fetchall()
    cursor3 = cur1.execute('SELECT fertility_age_women FROM birth_data2')
    fertility2 = cursor3.fetchall()
    list1 = []
    list2 = []
    totals = len(years2)
    i=0
    while i<totals:
        yy = years2[i][0]
        xx = fertility2[i][0]
        list1.append(yy)
        list2.append(xx)
        i+=1
    df1 = pd.DataFrame({
        'x': list1,
        'y': list2
    })
    chart_data2 = df1.to_dict(orient='records')
    return jsonify(chart_data2)
  
  
@app.route('/birth_map')
def part4():
    conn = sqlite3.connect("births.db")
    conn.row_factory = lambda cursor, row: row[0]
    cur = conn.cursor()
    cursor = cur.execute('SELECT DISTINCT YEAR FROM birthstate6 WHERE YEAR = 2020')
    years1 = cursor.fetchall()
    cursor1 = cur.execute('SELECT FERTILITY_RATE FROM birthstate6 WHERE YEAR = 2020')
    fertility_rate = cursor1.fetchall()
    cursor2 = cur.execute('SELECT DISTINCT STATE FROM birthstate6 WHERE YEAR = 2020')
    state = cursor2.fetchall()
    df = pd.DataFrame({
        'x': fertility_rate,
        'y': state
    })
    chart_data3 = df.to_dict(orient='records')
    return jsonify(chart_data3)
    

# @app.route('/drop1')
# def part5():
#     conn3 = sqlite3.connect("births.db")
#     cur3 = conn3.cursor()
#     a = cur3.execute('SELECT YEAR FROM birthstate6')
#     a1 = a.fetchall()
#     b = cur3.execute('SELECT STATE FROM birthstate6')
#     b1 = b.fetchall()
#     c = cur3.execute('SELECT BIRTHS FROM birthstate6')
#     c1 = c.fetchall()
#     list3 = []
#     list4 = []
#     list5 = []
#     total2 = len(a1)
#     i=0
#     while i<total2:
#         a2 = a1[i][0]
#         b2 = b1[i][0]
#         c2 = c1[i][0]
#         list3.append(a2)
#         list4.append(b2)
#         list5.append(c2)
#         i+=1
#     df3 = pd.DataFrame({
#         'x':list3,
#         'y':list4,
#         'z':list5
#     })
    
#     chart_data4 = df3.to_dict(orient='records')
#     return jsonify(chart_data4)
# conn1 = sqlite3.connect("birth_rate.db")
# cur1 = conn.cursor()
# cursor1 = cur.execute('SELECT * FROM birth_data2')
# items1 = cursor.fetchall()
# return render_template("births.html",items=items)
    return jsonify(all1)
    
    

if __name__ == '__main__':
    app.run(debug = True)