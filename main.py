from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


# Fonctions pour la base de données
def get_movies():
    db = sqlite3.connect('movies.db')
    c = db.cursor()
    c.execute("SELECT title FROM movies")
    movies = [row[0] for row in c.fetchall()]
    return movies


def get_movie(id):
    db = sqlite3.connect('movies.db')
    c = db.cursor()
    c.execute("SELECT * FROM movies WHERE id=?", (id,))
    movie = c.fetchone()
    if movie:
        return {'title': movie[1], 'year': movie[2], 'director': movie[3], 'genre': movie[4]}
    else:
        return {}


def search_movies(query):
    db = sqlite3.connect('movies.db')
    c = db.cursor()
    c.execute("SELECT title FROM movies WHERE title LIKE ?", ('%' + query + '%',))
    movies = [row[0] for row in c.fetchall()]
    return movies


# Routes Flask
@app.route('/movies', methods=['GET'])
def movies():
    # Récupérer tous les films depuis la base de données
    movies = get_movies()

    # Retourner la liste des films au format JSON
    return jsonify(movies)


@app.route('/movies/<int:id>', methods=['GET'])
def movie(id):
    # Récupérer le film avec l'ID donné depuis la base de données
    movie = get_movie(id)

    # Retourner les détails du film au format JSON
    return jsonify(movie)


@app.route('/movies/search', methods=['GET'])
def search():
    # Récupérer la requête de recherche depuis les paramètres de la requête
    query = request.args.get('q')

    # Rechercher les films correspondant à la requête dans la base de données
    results = search_movies(query)

    # Retourner les résultats de la recherche au format JSON
    return jsonify(results)


if __name__ == '__main__':
    app.run(port=7777)
