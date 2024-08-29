import socket
import sqlite3

from flask import Flask, render_template, request, jsonify


def read_sql():
    db = sqlite3.connect("mojabaza.db")
    cursor = db.cursor()
    cursor.execute("SELECT cover, title, author, description, link, ean, rate, notes FROM books;")
    result = cursor.fetchall()
    return result


app = Flask(__name__)


@app.route("/ksiazki")
def ksiazki():
    results = read_sql()
    return render_template("dodaj.html", results = results)


@app.route("/api", methods=["GET"])
def api_book():
    author = request.args.get("author")
    rate = request.args.get("rate")
    query = "SELECT title, author, link, rate, notes FROM books WHERE 1=1"
    args = []
    if author:
        query += " AND author LIKE '%'|| ? ||'%'"
        args.append(author)
    if rate:
        query += " AND rate >= ?"
        args.append(float(rate))

    db = sqlite3.connect("mojabaza.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute(query, args)
    book = cursor.fetchall()
    db.close()
    if book:
        return jsonify([dict(row) for row in book])


ip_server = (socket.gethostbyname(socket.gethostname()))

if __name__ == "__main__":
    app.run(debug=True, host=ip_server, port=5050)
