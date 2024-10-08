import socket
import sqlite3

from flask import Flask, render_template, request, jsonify


def read_sql(book_type):
    db = sqlite3.connect("mojabaza.db")
    cursor = db.cursor()
    cursor.execute("SELECT cover, title, author, description, link, ean, rate, notes FROM books WHERE type=?;", (book_type,))
    result = cursor.fetchall()
    return result


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("208.67.222.222", 80))  # Try to connect any site (here OpenDNS server), to check used ip address
    except:
        ip_address = "127.0.0.1"
        s.close()
        return ip_address
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


app = Flask(__name__)

@app.route("/")
@app.route("/ksiazki")
@app.route("/komiksy")
@app.route("/gry")
def ksiazki():
    if request.path == "/komiksy":
        results = read_sql("komiks")
    elif request.path == "/ksiazki":
        results = read_sql("książka")
    elif request.path == "/gry":
        results = read_sql("gra komputerowa")
    else:
        return render_template("dodaj.html")
    return render_template("dodaj.html", results = results)


@app.route("/api", methods=["GET"])
def api_book():
    author = request.args.get("author")
    rate = request.args.get("rate")
    tag = request.args.get("tag")
    category = request.args.get("category")

    query = "SELECT title, author, link, rate, notes FROM books WHERE 1=1"
    args = []
    if author:
        query += " AND author LIKE '%'|| ? ||'%'"
        args.append(author)
    if rate:
        query += " AND rate >= ?"
        args.append(float(rate))
    if tag:
        query += " AND (description LIKE '%'|| ? ||'%' OR notes LIKE '%'|| ? ||'%')"
        args.append(tag)
        args.append(tag)
    if category:
        query += " AND type=?"
        args.append(category)

    db = sqlite3.connect("mojabaza.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute(query, args)
    book = cursor.fetchall()
    db.close()
    if book:
        return jsonify([dict(row) for row in book])


host_ip = get_ip()

if __name__ == "__main__":
    app.run(debug=True, host=host_ip, port=5050)

