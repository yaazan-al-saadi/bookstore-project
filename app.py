from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        book_title TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == "POST":
        full_name = request.form["full_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        book_title = request.form["book_title"]

        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO orders (full_name, email, phone, book_title)
            VALUES (?, ?, ?, ?)
        """, (full_name, email, phone, book_title))
        conn.commit()
        conn.close()

        return render_template("order_success.html")

    return render_template("order.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        conn = sqlite3.connect("bookstore.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contacts (name, email, message)
            VALUES (?, ?, ?)
        """, (name, email, message))
        conn.commit()
        conn.close()

        return render_template("contact_success.html")

    return render_template("contact.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)