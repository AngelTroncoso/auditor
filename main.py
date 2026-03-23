import os
from crewai import Agent, Task, Crew, Process
from ingesta_pdf import procesar_normativa_chilena

# 1. Configuración del Modelo
os.environ["OPENAI_MODEL_NAME"] = 'gemini-1.5-pro' 

# 2. Definición de Agentes
agente_analista = Agent(
    role='Analista de Auditoría IFRS Chile',
    goal='Extraer y analizar datos financieros de archivos PDF según normativa local.',
    backstory='Experto en lectura de estados financieros y circulares del SII.',
    verbose=True
)

# ... (Tus otros agentes: Auditor y Estratega se mantienen igual)

# 3. Definición de Tareas con Variables Dinámicas
tarea_analisis = Task(
    description='''Analizar el contenido extraído del PDF: {contenido_pdf}. 
    Busca discrepancias con IFRS y normativas chilenas vigentes.''',
    expected_output='Informe técnico de hallazgos iniciales.',
    agent=agente_analista
)

# 4. Configuración de la Tripulación
auditoria_crew = Crew(
    agents=[agente_analista], # Añade aquí tus otros agentes
    tasks=[tarea_analisis],    # Añade aquí tus otras tareas
    process=Process.sequential
)

if __name__ == "__main__":
    print("## Sistema de Auditoría AI - Chile ##")
    ruta = input("Ingresa la ruta o nombre del PDF (ej: balance.pdf): ")
    
    if os.path.exists(ruta):
        # Usamos tu script de ingesta para convertir PDF a texto
        fragmentos = procesar_normativa_chilena(ruta)
        texto_completo = "\n".join([f.page_content for f in fragmentos])
        
        # Iniciamos la tripulación pasando el contenido dinámico
        result = auditoria_crew.kickoff(inputs={'contenido_pdf': texto_completo})
        print("\n--- RESULTADO DE AUDITORÍA ---")
        print(result)
    else:
        print("Error: El archivo no existe en la carpeta raíz.")