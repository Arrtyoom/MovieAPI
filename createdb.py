import sqlite3

# Establish a connection to a database
conn = sqlite3.connect('movies.db')

# Creer un objet curseur
c = conn.cursor()

# Creer une table nomme 'movies' avec les colomne pour id, title, release year, director, and genre
c.execute('''CREATE TABLE movies
             (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, genre TEXT)''')

# insertion des donnée dans la db
c.execute("INSERT INTO movies (title, year, director, genre) VALUES (?, ?, ?, ?)", ('The Godfather', 1972, 'Francis Ford Coppola', 'Crime/Drama'))
c.execute("INSERT INTO movies (title, year, director, genre) VALUES (?, ?, ?, ?)", ('The Shawshank Redemption', 1994, 'Frank Darabont', 'Drama'))
c.execute("INSERT INTO movies (title, year, director, genre) VALUES (?, ?, ?, ?)", ('The Dark Knight', 2008, 'Christopher Nolan', 'Action/Thriller'))

# "enregistr" les changement
conn.commit()

# Termine la connection
conn.close()
