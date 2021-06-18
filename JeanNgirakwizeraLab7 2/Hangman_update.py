import sqlite3
import Hangman_readone

# The update function updates an exiting item's data
def update():
    hiddenword = ""
    level = ""
    hint = ""
    hiddenword, level, hint = Hangman_readone.getWord()
    if hiddenword == "-1":
        print("Word not found")
    else:
        # Get the new values for item name and price
        level = input('New Level: ')
        hint = input('New Hint: ')
        correct = False
        while( not correct ):
            if level != 'E' and level != 'M' and level != 'H':
                print("Please enter an E, M, or H for level")
                level = input('New Level:')
            else:
                correct = True


        # Update the row
        num_updated = update_row(hiddenword, level, hint)
        print(f'{num_updated} row(s) updated')

#The update row function updates an existing row with a new
#ItemName and Price. The number of rows updated is returned
def update_row(name, level, hint):
    conn = None
    num_updated = 0
    try:
        conn = sqlite3.connect('hangmanwords.db')
        cur = conn.cursor()
        cur.execute('''UPDATE words
        SET level = ?, hint = ? WHERE lower(hiddenword) == ?''',
                    (level, hint, name.lower()))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return num_updated

#Execute the main function
if __name__ == '__main__':
    update()
