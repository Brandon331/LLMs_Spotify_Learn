🎧 Spotify for Learning - Generador de Snippets con IA 🤖
Este proyecto es el backend de una aplicación diseñada para transformar la manera en que aprendemos sobre la marcha. La API genera resúmenes educativos cortos y personalizados, y sugiere nuevos temas basados en los intereses del usuario, utilizando un potente modelo de lenguaje (LLM) y una arquitectura de Generación Aumentada por Recuperación (RAG).

🌟 Estado Actual del Proyecto
La lógica principal del backend está completa y funcional. Esto incluye:

Conexión a la base de datos SQLite.

Generación de resúmenes y sugerencias con Mistral y RAG.

Gestión de historial de usuarios.

Actualmente, toda esta funcionalidad se puede probar a través de un script de simulación. El siguiente paso es exponer esta lógica a través de una API web con FastAPI.

🏛️ Arquitectura Propuesta
El backend está construido con una arquitectura modular para separar responsabilidades, garantizando que el código sea limpio, mantenible y escalable.

🚀 API Framework (Próximo paso): FastAPI para crear endpoints rápidos y eficientes.

🗃️ Base de Datos: SQLite para almacenar información de usuarios, historial de aprendizaje y una base de conocimiento interna.

🧠 Modelo de Lenguaje (LLM): Mistral para la generación de texto.

🔐 Autenticación (Próximo paso): Tokens JWT para proteger los endpoints.

📚 Generación Aumentada por Recuperación (RAG): Se utiliza un enfoque híbrido para resúmenes y sugerencias.

📂 Estructura del Proyecto
main.py: (Futuro) Archivo principal de la API FastAPI.

llm_services.py: Contiene toda la lógica para interactuar con la API de Mistral.

database.py: Gestiona todas las interacciones con la base de datos SQLite.

auth.py: (Futuro) Manejará toda la seguridad y autenticación.

create_db.py: Script para inicializar la base de datos.

seed_db.py: Script para poblar la base de conocimiento para RAG.

full_simulation.py: Script para probar la lógica actual sin necesidad de una API web.

.env: Archivo para guardar claves secretas.

🚀 Configuración y Prueba (Simulación Local)
Sigue estos pasos para configurar y probar la lógica principal del proyecto en tu entorno local.

1. Prerrequisitos
Python 3.11 o superior.

2. Instalación
Clona el repositorio:

git clone [https://tu-repositorio.git](https://tu-repositorio.git)
cd LLMs_Spotify_Learn

(Recomendado) Crea y activa un entorno virtual:

python -m venv venv
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

Instala las dependencias:

pip install "mistralai" "passlib[bcrypt]" "python-jose[cryptography]" "fastapi[all]" "python-dotenv" "uvicorn"

Configura tus variables de entorno:
Crea un archivo llamado .env en la raíz del proyecto y añade tus claves.

# .env
MISTRAL_API_KEY="tu_api_key_de_mistral_aqui"
SECRET_KEY="tu_clave_secreta_para_jwt_muy_larga_y_segura"

Inicializa la Base de Datos:
Ejecuta este comando una sola vez para crear el archivo learning_app.db y sus tablas.

python create_db.py

(Opcional) Puebla la Base de Conocimiento:
Para probar la funcionalidad RAG, ejecuta este script.

python seed_db.py

3. Ejecutar la Simulación
En lugar de levantar un servidor web, ejecuta el script de simulación para ver la lógica en acción directamente en tu terminal.

python full_simulation.py

El script simulará a un usuario aprendiendo varios temas, mostrando los resúmenes generados, el historial actualizado y las sugerencias personalizadas.

📈 Próximos Pasos
El siguiente gran objetivo es conectar toda esta lógica a una API web para que pueda ser consumida por un frontend.
