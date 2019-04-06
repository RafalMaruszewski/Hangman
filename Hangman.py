import Database
import sqlite3
import random

conn = sqlite3.connect('hangman_db')
c = conn.cursor()
random_index = random.randrange(1,10)


bad_guesses_counter=0
def get_random_word():
    print("Selected random number: ", random_index)
    c.execute("SELECT word FROM words WHERE no=(?)", (random_index,))
    random_word = c.fetchone()
    print("Random word from database: ", random_word)
    return list(random_word)
    
def transform_word_to_str(random_word):
    random_w_str = ''.join(random_w)
    return random_w_str

random_w = get_random_word()
print("word:", random_w)
random_w_str = transform_word_to_str(random_w)
print("After transform: ", random_w_str)
empty_random_w_str = []
for i in range(len(random_w_str)):
    empty_random_w_str.append("_")
    
print(empty_random_w_str)

while True
    
    it1 = 0
    
    
    guess = input()
    for item in random_w_str:
        error_flag = 0
        if item == guess:
            print ("Zgadłeś literę ", guess)
            empty_random_w_str[it1] = guess
        else:
            error_flag = 1
    
        it1+=1
    
    if error_flag == 1:
        bad_guesses_counter += 1
        print("Liczba błędów: ", bad_guesses_counter)
    
        
    print(empty_random_w_str)