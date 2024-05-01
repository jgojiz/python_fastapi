# python_fastapi

run this command inside the directory where docker file is located
this creates the official postgres image with a volume
> docker build -t my_postgres_image .

then run this command to create the container and run any init files
> docker run -d -p 5432:5432 --name my_postgres_container my_postgres_image

if container already exists but not running, execute
> docker start container_name_or_id

go into the container using
> docker exec -it container_name_or_id bash

and once inside go to a specific database using
> psql -U root db_name

list all tables in the database
> \dt

After you've finished inspecting the database, you can exit the PostgreSQL CLI by typing
> \q

Then, exit the container's shell by typing
> exit

Finally, stop the container with
> docker stop name_or_id_container
