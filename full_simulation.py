import time
from app import database, llm_services

def simular_flujo_completo():
    # Usamos un nombre de usuario en lugar de un ID
    USUARIO_SIMULADO = "brandon_ejemplo"
    TEMAS_A_APRENDER = ["Homosapiens y materia negra"]

    print(f"🚀 INICIANDO SIMULACIÓN PARA EL USUARIO: {USUARIO_SIMULADO}")

    # 1. Aseguramos que el usuario exista en la DB
    database.add_or_get_user(USUARIO_SIMULADO)
    
    for tema in TEMAS_A_APRENDER:
        print(f"\n\n--- Aprendiendo sobre: '{tema}' ---")
        
        # a. Generar resumen
        resumen = llm_services.generar_resumen(tema)
        print("Resumen recibido:", f"\n   -> {resumen}")

        # b. Guardar en historial
        database.add_topic_to_history(USUARIO_SIMULADO, tema)
        print("\n   -> Tema guardado en el historial.")

        # c. Cargar historial actualizado
        historial_actual = database.get_user_history(USUARIO_SIMULADO)
        print("\nHistorial actual:")
        for item_historial in historial_actual:
            print(f"   - {item_historial}")

        # d. Generar sugerencias
        sugerencias = llm_services.sugerir_temas_relacionados(tema, historial_actual)
        print("\nSugerencias recibidas:")
        if sugerencias:
            for i, sug in enumerate(sugerencias, 1):
                print(f"   {i}. {sug}")
        else:
            print("   -> No se generaron sugerencias.")
        
        time.sleep(2)
        
    print("\n✅ SIMULACIÓN COMPLETADA")

if __name__ == "__main__":
    simular_flujo_completo()