from itertools import product
from BSteam.src.BSLogica import BSLogic

class TeamEvaluator:
    def __init__(self, data_categorizada, bayesian_network_manager, roles):
        self.data_categorizada = data_categorizada
        self.bayesian_network_manager = bayesian_network_manager
        self.roles = roles
        self.bs_logic = BSLogic()
        self.calcular_probabilidades()


    def calcular_probabilidades(self):
        predicciones = []
        for _, personaje in self.data_categorizada.iterrows():
            entrada_red = {
                'Meta': personaje['Meta'],
                'Pmap': personaje[f'Pmapa4'],  # Suponiendo mapa 4; cambiar si es dinámico
                'Vida Max': personaje['Vida'],
                'Daño Max': personaje['Daño'],
                'Rango Max': personaje['Rango'],
            }
            resultado = self.bayesian_network_manager.predecir(entrada_red)
            # Extraer la probabilidad de que sea el mejor personaje
            probabilidad_mejor = resultado[7].parameters[0]['si']
            predicciones.append(probabilidad_mejor)

        self.data_categorizada['Probabilidad Mejor'] = predicciones

        
    def generar_combinaciones(self):
        listas_por_rol = [
            self.data_categorizada[self.data_categorizada['Rol'] == rol][['Nombre', 'Probabilidad Mejor']].to_dict(orient='records')
            for rol in self.roles
        ]
        return list(product(*listas_por_rol))

    def evaluar_combinaciones(self, combinaciones):
        equipos_con_probabilidades = []

        for combinacion in combinaciones:
            nombres_equipo = [p['Nombre'] for p in combinacion]
            probabilidad_conjunta = (
                combinacion[0]['Probabilidad Mejor'] *
                combinacion[1]['Probabilidad Mejor'] *
                combinacion[2]['Probabilidad Mejor']
            )

            # Verificar sinergias y ajustar probabilidad
            self.bs_logic.knowledge.clear()
            for personaje in nombres_equipo:
                self.bs_logic.agregar_sinergias(personaje)

            sinergias = self.bs_logic.verificar_sinergias(nombres_equipo)
            ajuste_por_sinergias = 1 + (0.08 * sinergias)  # Ajuste del 8% por sinergia
            probabilidad_ajustada = probabilidad_conjunta * ajuste_por_sinergias

            equipos_con_probabilidades.append({
                'Rol1': nombres_equipo[0],
                'Rol2': nombres_equipo[1],
                'Rol3': nombres_equipo[2],
                'Probabilidad Conjunta': probabilidad_conjunta,
                'Probabilidad Ajustada': probabilidad_ajustada,
                'Sinergias': sinergias
            })

        return equipos_con_probabilidades
