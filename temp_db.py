import sqlite3


def create_table():
    db_connection = sqlite3.connect("mydb.db")
    db_cursor = db_connection.cursor()
    sql_command = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price text)"
    db_cursor.execute(sql_command)
    db_connection.commit()
    db_connection.close()


def check_records():
    db_connection = sqlite3.connect("mydb.db")
    db_cursor = db_connection.cursor()
    sql_command = "SELECT * FROM items WHERE name = 'chair'"
    db_cursor.execute(sql_command)
    result = db_cursor.fetchone()
    db_connection.close()
    return result


def insert_into_table():
    db_connection = sqlite3.connect("mydb.db")
    db_cursor = db_connection.cursor()
    sql_command = "INSERT INTO items (name, price) VALUES ('chair', '15.00'), ('table', '20.00')"
    db_cursor.execute(sql_command)
    db_connection.commit()
    db_connection.close()


def show_all():
    db_connection = sqlite3.connect("mydb.db")
    db_cursor = db_connection.cursor()
    sql_command = "SELECT * FROM items"
    db_cursor.execute(sql_command)
    result = db_cursor.fetchall()
    db_connection.close()
    for current_row in result:
        print(current_row)
