import psycopg2


def connect_db(env=""):
    try:
        conn = psycopg2.connect(
            host=env("DB_HOST"),
            port=env("DB_PORT"),
            database=env("DB_NAME"),
            user=env("DB_USER"),
            password=env("DB_PASS"),
        )
        print("✅ Successfully connected to the database.")

        cursor = conn.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
        )

        conn.commit()
        print("📦 'users' table is ready.")

        return conn
    except Exception as e:
        print("❌ An error occurred:", e)
        return None
