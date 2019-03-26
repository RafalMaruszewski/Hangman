import sqlite3

conn = sqlite3.connect('hangman_db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS words''')
c.execute('''CREATE TABLE IF NOT EXISTS words(no Integer, word text, points Integer)''')
c.execute("INSERT INTO words(no, word, points) VALUES(1, 'jablko', 6)")
c.execute("INSERT INTO words(no, word, points) VALUES(2, 'gruszka', 7)")
c.execute("INSERT INTO words(no, word, points) VALUES(3, 'pomarancz', 9)")
c.execute("INSERT INTO words(no, word, points) VALUES(4, 'mandarynka', 10)")
c.execute("INSERT INTO words(no, word, points) VALUES(5, 'grejpfrut', 9)")
c.execute("INSERT INTO words(no, word, points) VALUES(6, 'banan', 5)")
c.execute("INSERT INTO words(no, word, points) VALUES(7, 'liczi', 5)")
conn.commit()




conn.close()