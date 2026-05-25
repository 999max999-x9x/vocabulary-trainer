from database.connection import get_connection


def create_user(username, password):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO users(username, password_hash)
        VALUES(%s,%s)
        """,
        (username, password)
    )

    connection.commit()

    cursor.close()
    connection.close()

    print("Пользователь создан")


def get_users():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        """
    )

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users


def update_user(user_id, new_username):

    connection = get_connection()
    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE users
        SET username=%s
        WHERE id=%s
        """,

        (new_username, user_id)
    )


    connection.commit()


    cursor.close()
    connection.close()


    print("Пользователь обновлён")

def delete_user(user_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM users
        WHERE id=%s
        """,

        (user_id,)
    )


    connection.commit()


    cursor.close()
    connection.close()


    print("Пользователь удалён")
