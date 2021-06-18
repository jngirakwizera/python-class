import sqlite3


def read_data(searchString):
    print(searchString)
    conn = None
    results = []
    try:
        conn = sqlite3.connect('hangmanwords.db')
        cur = conn.cursor()
        cur.execute(searchString)
        results = cur.fetchall()
        print(results)
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return results


# The display_item function displays all items

def read_items():
    hiddenword = ""
    level = ""
    hint = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('hangmanwords.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM words ORDER BY hiddenword''')
        results = cur.fetchall()
        # print(results)
        # print(f'Hidden Word     Level     Hint')
        for row in results:
            hiddenword = row[0]
            level = row[1]
            hint = row[2]
            print(f'Hidden Word: {hiddenword}, Level: {level}, Hint: {hint}')
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

    # Return the number of matching rows.
    return hiddenword, level, hint
    # return results


def read_all_items():
    hiddenword = ""
    level = ""
    hint = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('hangmanwords.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM words ORDER BY hiddenword''')
        results = cur.fetchall()
        # print(results)
        # print(f'Hidden Word     Level     Hint')
        for row in results:
            hiddenword = row[0]
            level = row[1]
            hint = row[2]
            print(f'Hidden Word: {hiddenword}, Level: {level}, Hint: {hint}')
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

    # Return the number of matching rows.
    return results

if __name__ == '__main__':
    read_items()
