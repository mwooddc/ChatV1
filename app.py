import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('SQL/chat.db')
    ##To get the field headings from the table
    cursor = conn.execute('select * from users')
    #will assign field headings from table as a list of field headings
    names = list(map(lambda x: x[0], cursor.description))
    conn.row_factory = sqlite3.Row
    #return the connection and the field headings
    return conn, names

# db = sqlite3.connect('SQL/chat.db')

@app.route('/tester')
def tester():
    return render_template('tester.html')


@app.route('/registered', methods=["GET","POST"])
def registered():
    if request.method == "GET":
        conn, names = get_db_connection()
        #posts will store the results of the query
        posts = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        #pass the posts values through a variable called posts to the registered.html file
        #The posts (white) are here in this function
        #When they get recieved in the registered.html file they will be posts (orange)
        return render_template('registered.html', posts=posts, names=names)


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
            conn, names = get_db_connection()
            conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return redirect("/registered")

@app.route('/delete', methods=["GET","POST"])
def delete():
    conn, names = get_db_connection()
    if request.method == "POST":
        userID = request.form.get("the_userID_field")
        conn.execute("DELETE FROM users WHERE userID = ?",(userID,))
        ############################ comma REQUIRED here         ^
        conn.commit()
        conn.close()
        return redirect("/registered")

