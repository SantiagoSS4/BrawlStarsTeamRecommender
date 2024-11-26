import random

class SimulationManager:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def simular_partida(self, equipo, mapa_actual):
        df_inicial = self.data_processor.df_inicial
        resultados = []
        resultado_partida = random.choice([0, 1])  # 0: derrota, 1: victoria

        for personaje in equipo:
            indice_personaje = df_inicial[df_inicial['Nombre'] == personaje].index
            if not indice_personaje.empty:
                pmap_actual = df_inicial.at[indice_personaje[0], f'P{mapa_actual.lower()}']
                if resultado_partida == 1:  # Victoria
                    nuevo_pmap = min(pmap_actual + 0.03, 1.0)  # Incremento máximo hasta 1.0
                else:  # Derrota
                    nuevo_pmap = max(pmap_actual - 0.02, 0.0)  # Reducción mínima hasta 0.0

                # Actualizar el DataFrame
                df_inicial.at[indice_personaje[0], f'P{mapa_actual.lower()}'] = nuevo_pmap

                # Agregar resultado individual
                resultados.append({
                    'Personaje': personaje,
                    'Resultado': 'Victoria' if resultado_partida == 1 else 'Derrota',
                    'Pmap Actualizado': nuevo_pmap
                })

        # Guardar cambios en el CSV
        df_inicial.to_csv(self.data_processor.archivo_csv, index=False)

        return {
            'Resultado Equipo': 'Victoria' if resultado_partida == 1 else 'Derrota',
            'Resultados Individuales': resultados
        }