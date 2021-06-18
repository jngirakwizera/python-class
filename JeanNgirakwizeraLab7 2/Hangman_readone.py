import sqlite3

# The read function reads an existing item
def getWord():
    name = input('Enter word to search for: ')
    hiddenword, level, hint = read_item(name)
    if hiddenword == "":
        hiddenword = "-1"
    else:
        print(f'HiddenWord: {hiddenword:<20} Level: {level:<3}'
              f'Hint: {hint:<50}')
    return hiddenword, level, hint

# The display_item function displays all items
# with a matching ItemName
def read_item(name):
    hiddenword = ""
    level = ""
    hint = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('hangmanwords.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM words WHERE lower(hiddenword) == ?''', (name.lower(),))
        results = cur.fetchall()
        print(results)
        for row in results:
            hiddenword = row[0]
            level = row[1]
            hint = row[2]
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

    #Return the number of matching rows.
    return hiddenword, level, hint

if __name__ == '__main__':
    getWord()