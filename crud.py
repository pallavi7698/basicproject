from .db import get_connection
from .models import User

def create_user_in_db(user: User):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO user (id, name) VALUES (%s, %s)', (user.id, user.name))
    connection.commit()
    connection.close()

def get_user_from_db(user_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    connection.close()
    return user