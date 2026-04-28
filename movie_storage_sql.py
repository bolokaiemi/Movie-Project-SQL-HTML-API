import sqlite3

DB_NAME = "movies.db"


def connect():
    return sqlite3.connect(DB_NAME)


# =========================
# DATABASE SETUP
# =========================

def create_table():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                title TEXT PRIMARY KEY,
                year INTEGER,
                rating REAL,
                poster_url TEXT,
                trailer_url TEXT
            )
        """)


# =========================
# READ
# =========================

def list_movies():
    with connect() as conn:
        cursor = conn.execute("""
            SELECT title, year, rating, poster_url, trailer_url
            FROM movies
        """)

        movies = {}

        for title, year, rating, poster_url, trailer_url in cursor.fetchall():
            movies[title] = {
                "year": year,
                "rating": rating,
                "poster_url": poster_url,
                "trailer_url": trailer_url
            }

        return movies


# =========================
# CREATE
# =========================

def add_movie(title, year, rating, poster_url, trailer_url=None):
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO movies (title, year, rating, poster_url, trailer_url)
            VALUES (?, ?, ?, ?, ?)
            """,
            (title, year, rating, poster_url, trailer_url)
        )


# =========================
# DELETE
# =========================

def delete_movie(title):
    with connect() as conn:
        conn.execute("DELETE FROM movies WHERE title = ?", (title,))
        print("Movie deleted.")


# =========================
# UPDATE
# =========================

def update_movie(title, rating):
    with connect() as conn:
        conn.execute(
            "UPDATE movies SET rating = ? WHERE title = ?",
            (rating, title)
        )
        print("Movie updated.")