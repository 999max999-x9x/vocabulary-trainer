from database.connection import get_connection


def add_word(original_word,
             translation,
             example,
             collection_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO words(
            original_word,
            translation,
            example,
            collection_id
        )

        VALUES(%s,%s,%s,%s)
        """,

        (
            original_word,
            translation,
            example,
            collection_id
        )
    )


    connection.commit()

    cursor.close()
    connection.close()

    print("Слово добавлено")




def get_words():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM words
        """
    )


    words = cursor.fetchall()


    cursor.close()
    connection.close()


    return words

def update_word(word_id,
                new_translation):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE words
        SET translation=%s
        WHERE id=%s
        """,

        (
            new_translation,
            word_id
        )
    )


    connection.commit()


    cursor.close()
    connection.close()


    print("Слово обновлено")




def delete_word(word_id):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        DELETE FROM words
        WHERE id=%s
        """,

        (word_id,)
    )


    connection.commit()


    cursor.close()
    connection.close()


    print("Слово удалено")


def get_words_by_collection(
        collection_id
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *
        FROM words

        WHERE collection_id=%s
        """,

        (collection_id,)
    )


    words = cursor.fetchall()


    cursor.close()
    connection.close()


    return words