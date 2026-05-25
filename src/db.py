import sqlite3


def initialize_db(db_file_name):
    with sqlite3.connect(db_file_name) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                source TEXT NOT NULL,
                scraped_at TEXT NOT NULL
            )
        """)

        conn.commit()


def save_to_db(articles, db_file_name):
    with sqlite3.connect(db_file_name) as conn:
        cursor = conn.cursor()

        for article in articles:
            cursor.execute("""
                INSERT OR IGNORE INTO news (
                    title,
                    url,
                    source,
                    scraped_at
                ) VALUES (?, ?, ?, ?)
            """, (
                article["title"],
                article["url"],
                article["source"],
                article["scraped_at"],
            ))

        conn.commit()