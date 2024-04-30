# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set environment variables (optional)
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=my_movies

# Copy initialization SQL script to execute DDL on database startup
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432
