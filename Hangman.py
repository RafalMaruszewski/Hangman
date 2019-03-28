import Database
import sqlite3
import random

conn = sqlite3.connect('hangman_db')
c = conn.cursor()
#TODO: set range depends on database size
random_index = random.randrange(1,10)



def get_random_word():
    print("Selected random number: ", random_index)
    random_word = c.execute("SELECT word FROM words WHERE no=(?)", (random_index,))
    print("Random word from database: ", c.fetchone())
    return random_word
    
get_random_word()
   