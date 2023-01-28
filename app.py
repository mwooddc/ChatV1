import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('SQL/chat.db')
    conn.row_factory = sqlite3.Row
    return conn

# db = sqlite3.connect('SQL/chat.db')

@app.route('/registered')
def registered():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('registered.html', posts=posts)


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        #GET uses request.args.get()
        return render_template("index.html")
    elif request.method == "POST":
        #POST uses request.form.get()
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            return "<p>Hi</p>"
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect("/registered")
