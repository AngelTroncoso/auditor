import os
from crewai import Agent, Task, Crew, Process

# 1. Configuración del Modelo (Se usará Gemini Pro en la nube)
# Nota: La API Key se toma de las variables de entorno que configuraste en la web
os.environ["OPENAI_MODEL_NAME"] = 'gemini-1.5-pro' 

# 2. Definición de Agentes con precisión de Auditoría
agente_analista = Agent(
    role='Especialista Senior en Auditoría IFRS',
    goal='Detectar anomalías contables y discrepancias normativas en balances.',
    backstory='Experto en IFRS con enfoque en valoración de activos y reconocimiento de ingresos.',
    verbose=True,
    allow_delegation=False
)

agente_auditor = Agent(
    role='Gestor de Riesgos y Cumplimiento',
    goal='Validar la materialidad de los hallazgos y clasificar el riesgo.',
    backstory='Especialista en determinar si un error contable es material para la toma de decisiones.',
    verbose=True,
    allow_delegation=False
)

agente_estratega = Agent(
    role='CFO Digital y Estratega de Negocios',
    goal='Proponer optimizaciones financieras y soluciones de automatización con IA.',
    backstory='Ingeniero Comercial experto en eficiencia operativa y proyectos como BORAM.',
    verbose=True,
    allow_delegation=True
)

# 3. Definición de Tareas
tarea_analisis = Task(
    description='Analizar el balance financiero en busca de errores de clasificación IFRS.',
    expected_output='Lista técnica detallada de hallazgos contables.',
    agent=agente_analista
)

tarea_riesgo = Task(
    description='Evaluar los hallazgos anteriores y clasificarlos por criticidad.',
    expected_output='Informe de riesgos con hallazgos Críticos y Significativos resaltados.',
    agent=agente_auditor
)

tarea_estrategia = Task(
    description='Generar 3 recomendaciones estratégicas y una propuesta de automatización.',
    expected_output='Plan de acción financiero con enfoque en optimización de EBITDA.',
    agent=agente_estratega
)

# 4. Formación de la Tripulación (The Crew)
auditoria_crew = Crew(
    agents=[agente_analista, agente_auditor, agente_estratega],
    tasks=[tarea_analisis, tarea_riesgo, tarea_estrategia],
    process=Process.sequential, # Proceso secuencial para asegurar el flujo de info
    verbose=True
)

# 5. Ejecución (Para probar localmente o iniciar en la nube)
if __name__ == "__main__":
    print("## Iniciando Flujo de Auditoría IFRS ##")
    result = auditoria_crew.kickoff()
    print("\n\n########################")
    print("## RESULTADO FINAL ##")
    print(result)