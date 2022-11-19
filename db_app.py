# импорт необходимых библиотек и компонентов
import psycopg2
from config import host, user, password, db_name

# используемые переменные
doc_type = ''
user_id_doc = ''
new_user = ''
find_user = ''

# функция выводящая список таблицы users
def output_users_table():
    try:                                            # try/except конструкция для обработки исключений
        connection = psycopg2.connect(              # метод для подключения к БД
        host = host,
        user = user,
        password = password,
        database = db_name
    )
        connection.autocommit = True

        with connection.cursor() as cursor:         # cursor - обьект который содердит в себе методы для выполнения SQL запросов
            select_table_users = """select * from users;"""
            cursor.execute(select_table_users)
            all_records = cursor.fetchall()
            print('Таблица users')
            print('Всего записеей: ', len(all_records))
            print('Вывод каждой записи')
            for row in all_records:
                print('ID:', row[0])
                print('Имя:', row[1], end="\n\n")

    except Exception as _ex:                                                # обработка ошибок
            print("[INFO] Error while working with PostgreSQL", _ex)
    finally:                                                                # закрытие соединения
        if connection:
            connection.close()
            print("[INFO] PostreSQL connection closed")


# функция выводящая список таблицы doc

def output_doc_table():
    try:
        connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
        connection.autocommit = True

        with connection.cursor() as cursor:
            select_table_doc = """select * from doc;"""
            cursor.execute(select_table_doc)
            all_records = cursor.fetchall()
            print('Таблица doc')
            print('Всего записеей: ', len(all_records))
            print('Вывод каждой записи')
            for row in all_records:
                print('ID документа:', row[0])
                print('Номер документа:', row[1])
                print('Имя владельца:', row[2])
                print('Серия документа:', row[3], end="\n\n")

    except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostreSQL connection closed")

# создание нового документа

def create_new_doc():
    try:
        connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
        connection.autocommit = True

        with connection.cursor() as cursor:
            new_doc = f"""insert into doc (d_series, u_users_id) values ('{doc_type}', '{user_id_doc}');"""
            cursor.execute(new_doc)
        
    except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostreSQL connection closed")

# создание нового пользователя

def create_new_user():
    try:
        connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
        connection.autocommit = True

        with connection.cursor() as cursor:
            created_user = f"""insert into users (u_name) values ('{new_user}');"""
            cursor.execute(created_user)
        
    except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostreSQL connection closed")

# поиск пользователя и его документов

def find_user_in_db():
    try:
        connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
        connection.autocommit = True

        with connection.cursor() as cursor:
            find_in_db = f"""select users.u_name, users.u_id, doc.d_series from users 
                                join doc on users.u_id=doc.u_users_id where u_name = '{find_user}';"""
            cursor.execute(find_in_db)
            all_records = cursor.fetchall()
            for row in all_records:
                print('Имя пользователя:', row[0])
                print('ID пользователя:', row[1])
                print('Серия документа:', row[2], end="\n\n")
        
    except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostreSQL connection closed")


# меню для выбора действия

print('Выберите действие:','\n',
        '1. Вывести таблицу "users"','\n',
        '2. Вывести таблицу doc', '\n', 
        '3. Добавить документ','\n',
        '4. Добавление нового user-a','\n',
        '5. Поиск user-a'
        )
choose = int(input())



if choose == 1:

    output_users_table()

elif choose == 2:
    
    output_doc_table()

elif choose == 3:
    print('Введите тип документа:')
    doc_type = input()
    print('Введите ID пользователя:')
    user_id_doc = input()

    create_new_doc()

elif choose == 4:
    print('Введите имя добавляемого пользователя:')
    new_user = input()
    
    create_new_user()
    
elif choose == 5:
    print('Введите имя пользователя:')
    find_user = input()

    find_user_in_db()