from database.connection import get_connection


def create_progress(
        word_id,
        knowledge_level,
        repeat_date
):

    connection = get_connection()
    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO progress(

            word_id,
            knowledge_level,
            repeat_date

        )

        VALUES(%s,%s,%s)
        """,

        (
            word_id,
            knowledge_level,
            repeat_date
        )
    )


    connection.commit()

    cursor.close()
    connection.close()



def get_progress_by_word(
        word_id
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT *

        FROM progress

        WHERE word_id=%s
        """,

        (word_id,)
    )


    progress = cursor.fetchone()


    cursor.close()
    connection.close()


    return progress




def update_progress(
        progress_id,
        new_level
):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        UPDATE progress

        SET knowledge_level=%s

        WHERE id=%s
        """,

        (
            new_level,
            progress_id
        )
    )


    connection.commit()


    cursor.close()
    connection.close()




def get_all_collections_progress():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        SELECT

        collections.name,

        COUNT(words.id),

        COUNT(progress.word_id)


        FROM collections


        LEFT JOIN words

        ON words.collection_id =
        collections.id


        LEFT JOIN progress

        ON progress.word_id =
        words.id


        GROUP BY

        collections.name
        """
    )


    result = cursor.fetchall()


    cursor.close()
    connection.close()


    return result