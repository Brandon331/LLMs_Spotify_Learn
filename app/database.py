# En database.py
import sqlite3

DB_FILE = "learning_app.db"

def add_or_get_user(user_id: str):
    """Añade un usuario si no existe. No devuelve nada."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # 'OR IGNORE' evita un error si el user_id ya existe
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def add_topic_to_history(user_id: str, topic: str):
    """Añade un tema al historial de un usuario."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO learning_history (user_id, topic) VALUES (?, ?)", (user_id, topic))
    conn.commit()
    conn.close()

def get_user_history(user_id: str) -> list:
    """Obtiene el historial de un usuario."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT topic FROM learning_history WHERE user_id = ? ORDER BY learned_at DESC", (user_id,))
    temas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return temas

def create_user(username: str, hashed_password: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

def get_user_by_username(username: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT username, hashed_password FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_knowledge_by_topic(topic_key: str) -> str | None:
    """Busca y devuelve el contenido de un artículo por su clave de tema."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM knowledge_articles WHERE topic = ?", (topic_key,))
    result = cursor.fetchone() # fetchone() devuelve una tupla o None
    conn.close()
    if result:
        return result[0] # Devuelve solo el contenido (el primer elemento de la tupla)
    return None