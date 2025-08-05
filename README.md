# 🎧 Spotify for Learning - Generador de Snippets con IA 🤖

Este proyecto es el backend de una aplicación diseñada para transformar la manera en que aprendemos sobre la marcha. La API genera resúmenes educativos cortos y personalizados, y sugiere nuevos temas basados en los intereses del usuario, utilizando un potente modelo de lenguaje (LLM) y una arquitectura de Generación Aumentada por Recuperación (RAG).

---

## 🏛️ Arquitectura del Backend

El backend está construido con **FastAPI** y sigue una arquitectura modular para separar responsabilidades, garantizando que el código sea limpio, mantenible y escalable.

-   **🚀 API Framework**: **FastAPI** para crear endpoints rápidos y eficientes.
-   **🗃️ Base de Datos**: **SQLite** para almacenar información de usuarios, historial de aprendizaje y una base de conocimiento interna.
-   **🧠 Modelo de Lenguaje (LLM)**: **Mistral** para la generación de texto.
-   **🔐 Autenticación**: **Tokens JWT** para proteger los endpoints y gestionar las sesiones de usuario.
-   **📚 Generación Aumentada por Recuperación (RAG)**: Se utiliza un enfoque híbrido para resúmenes y sugerencias.

---

## 📂 Estructura del Proyecto

El proyecto está organizado con la lógica de la aplicación contenida dentro de un paquete `app`.

-   `main.py`: El punto de entrada principal de la API. Define los endpoints y orquesta las llamadas a los servicios de la aplicación.
-   `app/`: Paquete que contiene toda la lógica de negocio.
    -   `llm_services.py`: Contiene toda la lógica para interactuar con la API de Mistral.
    -   `database.py`: Gestiona todas las interacciones con la base de datos SQLite.
    -   `auth.py`: Maneja toda la seguridad y autenticación (hashing, JWTs).
    -   `create_db.py`: Script para inicializar la base de datos.
    -   `seed_db.py`: Script para poblar la base de conocimiento para RAG.
-   `learning_app.db`: El archivo de la base de datos SQLite.
-   `.env`: Archivo para guardar claves secretas (no se sube al repositorio).

---

## 🚀 Configuración y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el backend en tu entorno local.

### 1. Prerrequisitos

-   Python 3.11 o superior.

### 2. Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone [https://tu-repositorio.git](https://tu-repositorio.git)
    cd tu-proyecto
    ```

2.  **(Recomendado) Crea y activa un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install "mistralai" "passlib[bcrypt]" "python-jose[cryptography]" "fastapi[all]" "python-dotenv" "uvicorn"
    ```

4.  **Configura tus variables de entorno:**
    Crea un archivo llamado `.env` en la raíz del proyecto y añade tus claves.
    ```env
    # .env
    MISTRAL_API_KEY="tu_api_key_de_mistral_aqui"
    SECRET_KEY="tu_clave_secreta_para_jwt_muy_larga_y_segura"
    ```

5.  **Inicializa la Base de Datos:**
    Ejecuta este comando una sola vez desde la raíz del proyecto.
    ```bash
    python app/create_db.py
    ```

6.  **(Opcional) Puebla la Base de Conocimiento:**
    Para probar la funcionalidad RAG, ejecuta este script desde la raíz.
    ```bash
    python app/seed_db.py
    ```

### 3. Ejecutar el Servidor

Una vez completada la instalación, levanta el servidor de FastAPI con Uvicorn desde la raíz del proyecto.

```bash
uvicorn main:app --reload
