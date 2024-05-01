-- Create a new database called my_collections
CREATE DATABASE my_collections;

-- Connect to the newly created database
\c my_collections;

-- Create your table
CREATE TABLE my_movies (
    id SERIAL PRIMARY KEY,
    author VARCHAR(50),
    description VARCHAR(255),
    release_date VARCHAR(10)
);

-- Optionally, insert some initial data into the my_movies table
INSERT INTO my_movies (id, author, description, release_date) VALUES
    (1, 'author1', 'movie_description', '2024'),
    (2, 'author2', 'movie_description', '1990');
