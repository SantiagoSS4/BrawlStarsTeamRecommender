from Datos import DataProcessor
from RedBayesiana import BayesianNetworkManager
from Equipos import TeamEvaluator
from Feedback import SimulationManager

# Configuración inicial
archivo_csv = "base_datos_brawlstars.csv"
roles_por_mapa = {
    "Mapa1": ["Destructor", "Tanque", "Tiro de elite"],
    "Mapa2": ["Artilleria", "Control", "Apoyo"],
    "Mapa3": ["Asesino", "Tiro de elite", "Destructor"],
    "Mapa4": ["Control", "Tanque", "Apoyo"],
    "Mapa5": ["Asesino", "Artilleria", "Apoyo"]
}
# Pedir al usuario que seleccione un mapa
mapas_disponibles = ["Mapa1", "Mapa2", "Mapa3", "Mapa4", "Mapa5"]

print("Seleccione un mapa:")
for i, mapa in enumerate(mapas_disponibles, start=1):
    print(f"{i}. {mapa}")

while True:
    try:
        seleccion = int(input("Ingrese el número correspondiente al mapa (1-5): "))
        if 1 <= seleccion <= len(mapas_disponibles):
            mapa_seleccionado = mapas_disponibles[seleccion - 1]
            break
        else:
            print("Por favor, seleccione un número válido entre 1 y 5.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

print(f"\nHas seleccionado: {mapa_seleccionado}")
columnas = ["Meta", "Vida", "Daño", "Rango", "Pmapa1", "Pmapa2", "Pmapa3", "Pmapa4", "Pmapa5"]

# Procesar datos
data_processor = DataProcessor(archivo_csv, roles_por_mapa)
df_categorizado = data_processor.filtrar_y_categorizar_por_mapa(mapa_seleccionado, columnas)

# Configurar red bayesiana
bayesian_manager = BayesianNetworkManager()
bayesian_manager.configurar_red_bayesiana()

# Graficar la red bayesiana
bayesian_manager.graficar_red()

# Evaluar equipos
team_evaluator = TeamEvaluator(df_categorizado, bayesian_manager, roles_por_mapa[mapa_seleccionado])
combinaciones = team_evaluator.generar_combinaciones()
equipos = team_evaluator.evaluar_combinaciones(combinaciones)

# Seleccionar el mejor equipo
mejor_equipo = sorted(equipos, key=lambda x: x['Probabilidad Ajustada'], reverse=True)[0]

# Mostrar resultados del mejor equipo
print("Mejor equipo:")
print(mejor_equipo)

# Simular partida
simulation_manager = SimulationManager(data_processor)
resultados_simulacion = simulation_manager.simular_partida(
    [mejor_equipo['Rol1'], mejor_equipo['Rol2'], mejor_equipo['Rol3']],
    mapa_seleccionado
)

# Mostrar resultados de la simulación
print("\nResultados de la simulación:")
print(f"Resultado del equipo: {resultados_simulacion['Resultado Equipo']}")
print("Actualizaciones de probabilidades:")
for resultado in resultados_simulacion['Resultados Individuales']:
    print(f"- {resultado['Personaje']}: {resultado['Resultado']}, "
          f"Probabilidad en el mapa actualizada a {resultado['Pmap Actualizado']:.2f}")
