from database.connection import get_connection


def create_collection(name, user_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO collections(name, user_id)
        VALUES(%s,%s)
        """,

        (
            name,
            user_id
        )
    )


    connection.commit()


    cursor.close()
    connection.close()


    print("Коллекция создана")




def get_collections():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM collections
        """
    )


    collections = cursor.fetchall()


    cursor.close()
    connection.close()


    return collections




def update_collection(
        collection_id,
        new_name
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE collections
        SET name=%s
        WHERE id=%s
        """,

        (
            new_name,
            collection_id
        )
    )


    connection.commit()


    cursor.close()
    connection.close()


    print("Коллекция обновлена")




def delete_collection(
        collection_id
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM collections
        WHERE id=%s
        """,

        (collection_id,)
    )


    connection.commit()


    cursor.close()
    connection.close()


    print("Коллекция удалена")