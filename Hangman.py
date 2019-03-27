import Database
import sqlite3
import random

conn = sqlite3.connect('hangman_db')
c = conn.cursor()
#TODO: set range depends on database size
random_index = random.randrange(1,10)

print("Selected random number: ", random_index)
random_word = c.execute("SELECT word FROM words WHERE no=1", (random_index,))
print("Random word from database: ", c.fetchone())

def get_word(word):
    print("HI!")
    
#def get_random_word():
    
#    print (random_word)

#print(c.execute("SELECT * FROM words").fetchall())
   