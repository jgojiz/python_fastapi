from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from typing import List

app = FastAPI()

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}

conn = psycopg2.connect(**db_params)

class Movie(BaseModel):
    table: str
    id: int
    author: str
    description: bool
    release_date: str

@app.get('/movies')
def get_all_movies():
    movies = list()
    with conn.cursor() as cursor:
        try:
            query = 'SELECT * FROM movies_test;'
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                movies.append(row)
        except Exception as e:
            print(f"Error querying all movies: {e}")
    return {'movies': movies}

@app.get('/movies/{movieId}')
def get_movie(movieId):
    with conn.cursor() as cursor:
        try:
            query = f'SELECT * FROM movies_test WHERE id = {movieId};'
            cursor.execute(query)
            result = cursor.fetchall()
        except Exception as e:
            print(f"Error querying movie: {e}")
        if result:
            return {'movie': result}
    raise HTTPException(status_code=404, detail= "Id not found.")