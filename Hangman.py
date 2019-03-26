import Database
import sqlite3

conn = sqlite3.connect('hangman_db')
c = conn.cursor()

def get_word(word):
    print("HI!")

print(c.execute("SELECT * FROM words").fetchall())
    
get_word('lord')