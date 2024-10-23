# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Create a database table if it doesn't exist
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, info TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT info FROM data")
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=[row[0] for row in rows])

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json['data']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (info) VALUES (?)", (data,))
    conn.commit()
    conn.close()
    return jsonify(success=True)

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
