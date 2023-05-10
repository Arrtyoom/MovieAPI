import sqlite3

# Establish a connection to a database
conn = sqlite3.connect('movies.db')

# Create a cursor object
c = conn.cursor()

# Create a table named 'movies' with columns for movie id, title, release year, director, and genre
c.execute('''CREATE TABLE movies
             (id INTEGER PRIMARY KEY, title TEXT, year INTEGER, director TEXT, genre TEXT)''')

# Insert data into the 'movies' table
c.execute("INSERT INTO movies (title, year, director, genre) VALUES (?, ?, ?, ?)", ('The Godfather', 1972, 'Francis Ford Coppola', 'Crime/Drama'))
c.execute("INSERT INTO movies (title, year, director, genre) VALUES (?, ?, ?, ?)", ('The Shawshank Redemption', 1994, 'Frank Darabont', 'Drama'))
c.execute("INSERT INTO movies (title, year, director, genre) VALUES (?, ?, ?, ?)", ('The Dark Knight', 2008, 'Christopher Nolan', 'Action/Thriller'))

# Commit the changes
conn.commit()

# Close the connection
conn.close()
