import sqlite3


def link_validation(link):
    try:
        if link.startswith("https://lubimyczytac.pl/ksiazka/") or link.startswith("https://www.gry-online.pl/gry/"):
            return True
        else:
            return False
    except AttributeError:
        return False


def is_item_in_database(link):
    db = sqlite3.connect("mojabaza.db")
    cursor = db.cursor()
    cursor.execute("SELECT * from books WHERE link = ?", (link,))
    book = cursor.fetchall()
    db.close()
    if book:
        return True
    else:
        return False

def select_category(link):
    if link.startswith("https://lubimyczytac.pl/ksiazka/"):
        return "books"
    else:
        return "games"
