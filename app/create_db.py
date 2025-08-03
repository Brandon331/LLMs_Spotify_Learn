import sqlite3

def create_database():
    conn = sqlite3.connect('learning_app.db')
    cursor = conn.cursor()

    # Crear la tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        hashed_password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Crear la tabla del historial de aprendizaje
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS learning_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        topic TEXT NOT NULL,
        learned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    );
    """)

    print("Base de datos y tablas creadas con éxito.")


        # Crear la tabla para la base de conocimiento de RAG
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_articles (
        topic TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    create_database()