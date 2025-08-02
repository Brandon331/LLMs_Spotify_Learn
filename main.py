import os
from mistralai import Mistral, UserMessage
from dotenv import load_dotenv

load_dotenv()

def llamar_a_mistral(prompt_del_usuario: str):
    try:
        api_key = os.environ.get("MISTRAL_API_KEY")
        if not api_key:
            return "Error: La MISTRAL_API_KEY no fue encontrada."

        client = Mistral(api_key=api_key)
        
        messages = [
            {"role": "user", "content": prompt_del_usuario}
        ]

        respuesta = client.chat.complete(
            model="mistral-small-latest",
            messages=messages
        )
        
        return respuesta.choices[0].message.content

    except Exception as e:
        return f"Ha ocurrido un error: {e}"

if __name__ == "__main__":
    tema = input('Dime de que quieres aprender: ')
    #850 - 950 palabras sera por el momento 25 a 50 palabras, para las pruebas
    #Esto es crucial para que la narración dure unos 5 minutos, que es el objetivo del proyecto.
    prompt = f""" Actúa como un narrador experto y carismático para un podcast educativo llamado "Spotify for Learning". Tu tarea es generar un guion de audio sobre un tema específico.
El guion debe ser informativo, fácil de seguir y atractivo para una audiencia general.
### REQUISITOS OBLIGATORIOS:
1.  **Rol y Tono**: Asume el rol de un presentador de podcast entusiasta y claro. El tono debe ser conversacional, curioso y evitar jerga compleja. Imagina que se lo explicas a un amigo inteligente.
2.  **Estructura del Contenido**: Organiza la explicación siguiendo estrictamente el formato "¿Qué es?", "¿Por qué es importante?" y "¿Cómo funciona/ocurrió?". Esta estructura es fundamental.
3.  **Duración y Longitud**: El guion debe tener una longitud aproximada de 25-50 palabras. 
4.  **Formato de Salida**: Proporciona únicamente el texto del guion. No incluyas títulos, encabezados como "Introducción" o "Conclusión", ni ningún comentario adicional. El texto debe estar listo para ser enviado directamente a un motor de Texto-a-Voz.
5.  **Gancho Inicial**: Comienza siempre con una pregunta o un dato sorprendente para captar la atención del oyente desde el primer segundo.
### TEMA DEL GUION DE HOY:
{tema}"""
    resultado = llamar_a_mistral(prompt)
    
    print("Prompt enviado a Mistral:")
    print(prompt)
    print("\nRespuesta de Mistral:")
    print(resultado)