# ejecutar la imagen de postgress antes de ejecutar esta prueba
import psycopg2

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}

conn = psycopg2.connect(**db_params)
print("Conexión exitosa.")


try:
    # Create a cursor
    cursor = conn.cursor()

    # Define the SQL statement to create a table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS movies_test (
        id SERIAL PRIMARY KEY,
        task VARCHAR(255),
        completed BOOL
    );
    '''

    # Execute the SQL statement to create the table
    cursor.execute(create_table_query)

    # Commit changes
    conn.commit()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed.")