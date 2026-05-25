from datetime import date
import random


from services.collection_service import (
    create_collection,
    get_collections
)

from services.user_service import (
    create_user,
    get_users
)

from services.word_service import (
    add_word,
    get_words,
    get_words_by_collection,
    delete_word
)

from services.progress_service import (
    create_progress,
    update_progress,
    get_progress_by_word,
    get_all_collections_progress
)


while True:

    print("""

1 - создать пользователя
2 - показать пользователей

3 - создать коллекцию
4 - показать коллекции

5 - добавить слово
6 - показать слова
7 - удалить слово

8 - начать тренировку
9 - показать прогресс

0 - выход

""")

    choice = input(
        "Выберите действие: "
    )


    # СОЗДАТЬ ПОЛЬЗОВАТЕЛЯ

    if choice == "1":

        username = input(
            "Введите имя: "
        )

        password = input(
            "Введите пароль: "
        )

        create_user(
            username,
            password
        )


    # ПОКАЗАТЬ ПОЛЬЗОВАТЕЛЕЙ

    elif choice == "2":

        users = get_users()

        print("\nПользователи:\n")

        for index, user in enumerate(
                users,
                start=1
        ):

            print(

                f"{index} - {user[1]}"

            )


    # СОЗДАТЬ КОЛЛЕКЦИЮ

    elif choice == "3":

        users = get_users()

        print("\nПользователи:\n")

        for index, user in enumerate(

                users,

                start=1

        ):

            print(

                f"{index} - {user[1]}"

            )

        choice_user = int(

            input(

                "\nВыберите пользователя: "

            )

        )

        selected_user = (

            users[choice_user - 1]

        )


        name = input(

            "Название коллекции: "

        )


        create_collection(

            name,

            selected_user[0]

        )


    # ПОКАЗАТЬ КОЛЛЕКЦИИ

    elif choice == "4":

        collections = get_collections()

        print(

            "\nКоллекции:\n"

        )

        for index, collection in enumerate(

                collections,

                start=1

        ):

            print(

                f"{index} - {collection[1]}"

            )


    # ДОБАВИТЬ СЛОВО

    elif choice == "5":

        collections = get_collections()

        print(

            "\nКоллекции:\n"

        )

        for index, collection in enumerate(

                collections,

                start=1

        ):

            print(

                f"{index} - {collection[1]}"

            )


        selected = int(

            input(

                "\nВыберите коллекцию: "

            )

        )


        collection = (

            collections[selected - 1]

        )


        original = input(

            "Слово: "

        )

        translation = input(

            "Перевод: "

        )

        example = input(

            "Пример: "

        )


        add_word(

            original,

            translation,

            example,

            collection[0]

        )


    # ПОКАЗАТЬ СЛОВА

    elif choice == "6":

        words = get_words()

        print(

            "\nСлова:\n"

        )


        for index, word in enumerate(

                words,

                start=1

        ):

            print(

f"""
{index}

Слово:
{word[1]}

Перевод:
{word[2]}

-------------
"""
            )


    # УДАЛИТЬ СЛОВО

    elif choice == "7":

        words = get_words()


        print(

            "\nСлова:\n"

        )


        for index, word in enumerate(

                words,

                start=1

        ):

            print(

                f"{index} - {word[1]}"

            )


        choice_word = int(

            input(

                "\nВыберите слово: "

            )

        )


        selected_word = (

            words[choice_word - 1]

        )


        delete_word(

            selected_word[0]

        )


    # ТРЕНИРОВКА

    elif choice == "8":

        collections = get_collections()


        print(

            "\nКоллекции:\n"

        )


        for index, collection in enumerate(

                collections,

                start=1

        ):

            print(

                f"{index} - {collection[1]}"

            )


        selected = input(

"""
Выберите коллекции:

Например:

1,2

>

"""
        )


        selected_indexes = [

            int(i.strip()) - 1

            for i in selected.split(",")

        ]


        words = []


        for index in selected_indexes:


            collection_id = (

                collections[index][0]

            )


            collection_words = (

                get_words_by_collection(

                    collection_id

                )

            )


            words.extend(

                collection_words

            )


        random.shuffle(

            words

        )


        if len(words) == 0:

            print(

                "Нет слов"

            )

            continue


        correct = 0


        for word in words:


            answer = input(

f"""

Переведите:

{word[1]}

>

"""
            ).strip()


            if answer.strip().lower() == (

                    word[2].strip().lower()

            ):


                print(

                    "Верно"

                )


                correct += 1


                progress = (

                    get_progress_by_word(

                        word[0]

                    )

                )


                if progress:


                    update_progress(

                        progress[0],

                        progress[2] + 1

                    )


                else:


                    create_progress(

                        word[0],

                        1,

                        date.today()

                    )


            else:


                print(

f"""

Неверно

Правильный ответ:

{word[2]}

Пример:

{word[3]}

"""
                )


        print(

f"""

Результат:

{correct}/{len(words)}

"""

        )


    # ПРОГРЕСС

    elif choice == "9":

        progress = (

            get_all_collections_progress()

        )


        for item in progress:


            collection = item[0]

            total = item[1]

            passed = item[2]


            if total == 0:

                percent = 0

            else:

                percent = round(

                    passed /
                    total *
                    100

                )


            print(

f"""
Коллекция:

{collection}


Пройдено:

{passed}/{total}


Прогресс:

{percent}%


------------------
"""
            )


    elif choice == "0":

        print(

            "Выход"

        )

        break