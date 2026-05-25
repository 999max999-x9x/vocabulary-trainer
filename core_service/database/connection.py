import psycopg2


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="vocab_db",
        user="admin",
        password="admin123",
        port=5432
    )
