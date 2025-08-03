# En database.py
import sqlite3

DB_FILE = "learning_app.db"

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

def add_or_get_user(username: str):
    """Añade un usuario si no existe (con una contraseña de prueba para la simulación)."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Usamos un hash de contraseña vacío por simplicidad en la simulación
    hashed_password = "dummy_password_for_simulation" 
    cursor.execute("INSERT OR IGNORE INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()

def add_topic_to_history(username: str, topic: str):
    """
    Añade un tema al historial de un usuario.
    Usa 'INSERT OR IGNORE' para evitar errores si el tema ya existe para ese usuario.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO learning_history (user_id, topic) VALUES (?, ?)", (username, topic))
    conn.commit()
    conn.close()

def get_user_history(username: str) -> list:
    """Obtiene el historial de un usuario, ordenado del más reciente al más antiguo."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT topic FROM learning_history WHERE user_id = ? ORDER BY learned_at DESC", (username,))
    temas = [row[0] for row in cursor.fetchall()]
    conn.close()
    return temas

def get_knowledge_by_topic(topic_key: str) -> str | None:
    """Busca y devuelve el contenido de un artículo por su clave de tema."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM knowledge_articles WHERE topic = ?", (topic_key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
