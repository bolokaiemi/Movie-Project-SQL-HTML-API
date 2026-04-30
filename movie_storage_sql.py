import sqlite3

DB_NAME = "movies.db"


# =========================
# CONNECTION
# =========================
def connect():
    return sqlite3.connect(DB_NAME)


# =========================
# CREATE TABLES
# =========================
def create_table():
    conn = connect()
    cur = conn.cursor()

    # USERS TABLE
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    """)

    # MOVIES TABLE (base structure ONLY)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            year INTEGER,
            rating REAL
        )
    """)

    # =========================
    # SAFE COLUMN ADDITIONS
    # =========================

    # 🔑 Fix for your error
    try:
        cur.execute("ALTER TABLE movies ADD COLUMN user_id INTEGER")
    except sqlite3.OperationalError:
        pass

    try:
        cur.execute("ALTER TABLE movies ADD COLUMN poster TEXT")
    except sqlite3.OperationalError:
        pass

    try:
        cur.execute("ALTER TABLE movies ADD COLUMN trailer TEXT")
    except sqlite3.OperationalError:
        pass

    try:
        cur.execute("ALTER TABLE movies ADD COLUMN note TEXT")
    except sqlite3.OperationalError:
        pass

    try:
        cur.execute("ALTER TABLE movies ADD COLUMN country TEXT")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()


# =========================
# USERS FUNCTIONS
# =========================
def list_users():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users")
    users = cur.fetchall()

    conn.close()
    return users


def add_user(name):
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print("User already exists.")

    conn.close()


def get_user(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users WHERE id = ?", (user_id,))
    user = cur.fetchone()

    conn.close()
    return user


# =========================
# MOVIES FUNCTIONS
# =========================
def list_movies(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT title, year, rating, poster, trailer, note, country
        FROM movies
        WHERE user_id = ?
    """, (user_id,))

    rows = cur.fetchall()
    conn.close()

    movies = {}
    for row in rows:
        movies[row[0]] = {
            "year": row[1],
            "rating": row[2],
            "poster": row[3],
            "trailer": row[4],
            "note": row[5],
            "country": row[6]
        }

    return movies


def add_movie(user_id, title, year, rating, poster="", trailer="", note="", country=""):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO movies (user_id, title, year, rating, poster, trailer, note, country)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, title, year, rating, poster, trailer, note, country))

    conn.commit()
    conn.close()


def delete_movie(user_id, title):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM movies
        WHERE title = ? AND user_id = ?
    """, (title, user_id))

    conn.commit()
    conn.close()


def update_movie_note(user_id, title, note):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        UPDATE movies
        SET note = ?
        WHERE title = ? AND user_id = ?
    """, (note, title, user_id))

    conn.commit()
    conn.close()


def update_movie_rating(user_id, title, rating):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        UPDATE movies
        SET rating = ?
        WHERE title = ? AND user_id = ?
    """, (rating, title, user_id))

    conn.commit()
    conn.close()