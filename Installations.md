pip install fastapi uvicorn
<!-- If using SQLite/PostgreSQL, install SQLAlchemy: -->
pip install sqlalchemy psycopg2
<!-- Add Security Utils (utils/security.py)
For password hashing, install bcrypt: -->
pip install passlib[bcrypt]
pip install pydantic[email] or pip install email-validator


<!-- Environment Variables (.env)
Install python-dotenv: -->
pip install python-dotenv

<!-- to run  -->
uvicorn app.main:app --reload


<!-- install all required modules -->
pip install -r requirements.txt



<!-- application run on -->
http://127.0.0.1:8000