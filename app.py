from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from typing import List

app = FastAPI()

db_params = {
    'dbname': 'my_collections',
    'user': 'root',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}

conn = psycopg2.connect(**db_params)

class Movie(BaseModel):
    table: str
    id: int
    author: str
    description: str
    release_date: str

@app.get('/movies')
def get_all_movies():
    movies = list()
    with conn.cursor() as cursor:
        try:
            query = 'SELECT * FROM my_movies;'
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                movies.append(row)
        except Exception as e:
            print(f"Error querying all movies: {e}")
    return {'movies': movies}

@app.get('/movie/{movieId}')
def get_movie(movieId):
    with conn.cursor() as cursor:
        try:
            query = f'SELECT * FROM my_movies WHERE id = {movieId};'
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            print(f"Error querying movie: {e}")
        if result:
            return {'movie': result}
    raise HTTPException(status_code=404, detail= "Id not found.")

@app.post('/movie')
def create_movie(movie: Movie):
    with conn.cursor() as cursor:
        try:
            query = f"""
                INSERT INTO {movie.table} (id, author, description, release_date) 
                VALUES (%s, %s, %s, %s)
            """
            print(query)
            print((movie.id, movie.author, movie.description, movie.release_date))
            cursor.execute(query, (movie.id, movie.author, movie.description, movie.release_date))
            conn.commit()
        except Exception as e:
            print(f"Error creating movie: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
    return {'response': 'Movie created!'}

from fastapi import HTTPException

@app.put('/movie')
def update_movie(movie: Movie):
    with conn.cursor() as cursor:
        try:
            query = f"""
                UPDATE {movie.table} 
                SET author = %s, description = %s, release_date = %s
                WHERE id = %s
            """
            cursor.execute(query, (movie.author, movie.description, movie.release_date, movie.id))
            conn.commit()
        except Exception as e:
            print(f"Error updating movie: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
    return {'response': 'Movie updated!'}

from fastapi import HTTPException

@app.delete('/movie')
def delete_movie(movie: Movie):
    with conn.cursor() as cursor:
        try:
            query = f"""
                DELETE FROM {movie.table} 
                WHERE id = %s
            """
            cursor.execute(query, (movie.id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Movie not found")
        except Exception as e:
            print(f"Error deleting movie: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
    return {'response': 'Movie deleted successfully'}

