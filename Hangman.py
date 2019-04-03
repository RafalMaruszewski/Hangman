import Database
import sqlite3
import random

conn = sqlite3.connect('hangman_db')
c = conn.cursor()
#TODO: set range depends on database size
random_index = random.randrange(1,10)


bad_guesses_counter=0
def get_random_word():
    print("Selected random number: ", random_index)
    c.execute("SELECT word FROM words WHERE no=(?)", (random_index,))
    random_word = c.fetchone()
    print("Random word from database: ", random_word)
    return list(random_word)
    
def make_a_guess(random_word):
    guess = input()
    guess = guess.lower()
    #for item in random_word:
    #    for letter in item:
    #        if guess == letter:
    #            print("+1") 
    #        else:
    #            print("Błąd!")

random_w = get_random_word()
print("word:", random_w)
random_w_str = ''.join(random_w)
print("After transform: ", random_w_str)
for i in range(len(random_w_str)):
    print("_", end = " ")
make_a_guess(random_w)
