<!-- Manually Create the Table in pgAdmin
If you want to manually create the table, run the following SQL in pgAdmin: -->
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password TEXT NOT NULL
);


<!-- to see the table fields details in query in pgadmin -->
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users';
