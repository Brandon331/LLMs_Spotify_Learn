import sqlite3

def create_database():
    """
    Crea la base de datos y las tablas con las restricciones correctas.
    La tabla 'learning_history' ahora previene duplicados.
    """
    conn = sqlite3.connect('learning_app.db')
    cursor = conn.cursor()

    # --- Tabla de usuarios ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        hashed_password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # --- Tabla del historial con REGLA ANTI-DUPLICADOS ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS learning_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        topic TEXT NOT NULL,
        learned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (username),
        -- Añadimos esta línea para evitar que un usuario tenga el mismo tema dos veces
        UNIQUE(user_id, topic) 
    );
    """)

    # --- Tabla de conocimiento ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_articles (
        topic TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    print("Base de datos y tablas creadas/actualizadas con éxito.")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
