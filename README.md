# 🎧 Spotify for Learning - Generador de Snippets con IA 🤖

Este proyecto es el backend de una aplicación diseñada para transformar la manera en que aprendemos sobre la marcha. La API genera resúmenes educativos cortos y personalizados, y sugiere nuevos temas basados en los intereses del usuario, utilizando un potente modelo de lenguaje (LLM) y una arquitectura de Generación Aumentada por Recuperación (RAG).

---

## 🏛️ Arquitectura del Backend

El backend está construido con **FastAPI** y sigue una arquitectura modular para separar responsabilidades, garantizando que el código sea limpio, mantenible y escalable.

-   **🚀 API Framework**: **FastAPI** para crear endpoints rápidos y eficientes.
-   **🗃️ Base de Datos**: **SQLite** para almacenar información de usuarios, historial de aprendizaje y una base de conocimiento interna.
-   **🧠 Modelo de Lenguaje (LLM)**: **Mistral** para la generación de texto (resúmenes y sugerencias).
-   **🔐 Autenticación**: **Tokens JWT** para proteger los endpoints y gestionar las sesiones de usuario.
-   **📚 Generación Aumentada por Recuperación (RAG)**: Se utiliza un enfoque híbrido:
    1.  Para los **resúmenes**, el sistema primero intenta recuperar información de una base de conocimiento interna para dar respuestas precisas y controladas. Si no encuentra información, recurre al conocimiento general del LLM.
    2.  Para las **sugerencias**, el sistema recupera el historial de aprendizaje del usuario para generar recomendaciones verdaderamente personalizadas.

---

## 📂 Estructura del Proyecto

El backend está organizado en los siguientes módulos:

-   `main.py`: El archivo principal que define los endpoints de la API (`/register`, `/token`, `/learn/`).
-   `llm_services.py`: Contiene toda la lógica para interactuar con la API de Mistral.
-   `database.py`: Gestiona todas las interacciones con la base de datos SQLite.
-   `auth.py`: Maneja toda la seguridad y autenticación.
-   `create_db.py`: Script para inicializar la base de datos.
-   `seed_db.py`: Script para poblar la base de conocimiento para RAG.
-   `.env`: Archivo para guardar claves secretas (no se sube al repositorio).

---

## 🚀 Configuración y Puesta en Marcha

Sigue estos pasos para configurar y ejecutar el backend en tu entorno local.

### 1. Prerrequisitos
- Python 3.11 o superior.

### 2. Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone [https://tu-repositorio.git](https://tu-repositorio.git)
    cd LLMs_Spotify_Learn
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
    Ejecuta este comando una sola vez para crear el archivo `learning_app.db` y sus tablas.
    ```bash
    python create_db.py
    ```

6.  **(Opcional) Puebla la Base de Conocimiento:**
    Para probar la funcionalidad RAG, ejecuta este script.
    ```bash
    python seed_db.py
    ```

### 3. Ejecutar el Servidor

Levanta el servidor de FastAPI con Uvicorn.

```bash
uvicorn main:app --reload
El servidor estará disponible en http://127.0.0.1:8000. Puedes acceder a la documentación interactiva de la API en http://127.0.0.1:8000/docs.🔗 Endpoints de la APIAutenticaciónPOST /registerRegistra un nuevo usuario.Body (form-data): username, password.Respuesta: Mensaje de confirmación.POST /tokenInicia sesión y devuelve un token de acceso.Body (form-data): username, password.Respuesta: { "access_token": "...", "token_type": "bearer" }.Funcionalidad PrincipalPOST /learn/Genera un resumen de un tema y sugerencias personalizadas.Endpoint protegido. Requiere autenticación.Header: Authorization: Bearer <tu_token_jwt>Parámetro de URL: ?tema=El+Tema+Que+Quieres+AprenderRespuesta:{
  "usuario": "nombre_del_usuario",
  "tema_aprendido": "El Tema Que Quieres Aprender",
  "resumen": "El resumen generado por el LLM...",
  "sugerencias_para_ti": [
    "Sugerencia 1",
    "Sugerencia 2",
    "Sugerencia 3",
    "Sugerencia 4",
    "Sugerencia 5"
  ]
}
