import sqlite3


def create():
    print('Create New Hidden Word')
    name = input('Hidden Word: ')
    if (len(name) > 10):
        level = "H"
    elif (len(name)) > 5:
        level = "M"
    else:
        level = "E"

    hint = input('Hint:')
    insert_row(name, level, hint)


# The insert_row function inserts a row into the Inventory table.
def insert_row(name, level, hint):
    conn = None
    try:
        conn = sqlite3.connect('hangmanwords.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS words ( hiddenword TEXT PRIMARY KEY NOT NULL, level TEXT NOT NULL, hint TEXT )''')
        cur.execute('''INSERT INTO words (hiddenword, level, hint) VALUES (?,?,?)''', (name, level, hint))
        conn.commit()
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn is not None:
            conn.close()

    # Execute the main function.


if __name__ == '__main__':
    create()
