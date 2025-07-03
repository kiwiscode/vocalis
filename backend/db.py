import psycopg2


def connect_db(env):
    try:
        conn = psycopg2.connect(
            host=env("DB_HOST"),
            port=env("DB_PORT"),
            database=env("DB_NAME"),
            user=env("DB_USER"),
            password=env("DB_PASS"),
        )
        print("✅ Successfully connected to the database.")
        return conn
    except Exception as e:
        print("❌ An error occurred:", e)
        return None


#  cursor = conn.cursor()

#     cursor.execute(
#         """
#         CREATE TABLE IF NOT EXISTS users (
#             id SERIAL PRIMARY KEY,
#             name VARCHAR(100),
#             email VARCHAR(100)
#         )
#     """
#     )
#     conn.commit()
#     print("📦 'users' table is ready.")
