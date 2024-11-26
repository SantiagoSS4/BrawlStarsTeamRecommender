import networkx as nx
import matplotlib.pyplot as plt
from pomegranate import BayesianNetwork, DiscreteDistribution, ConditionalProbabilityTable, Node

class BayesianNetworkManager:
    def __init__(self):
        self.model = None

    def configurar_red_bayesiana(self):
        meta = DiscreteDistribution({'bajo': 0.2, 'medio': 0.5, 'alto': 0.3})
        pmap = DiscreteDistribution({'bajo': 0.3, 'medio': 0.4, 'alto': 0.3})
        vida_max = DiscreteDistribution({'bajo': 0.4, 'medio': 0.4, 'alto': 0.2})
        daño_max = DiscreteDistribution({'bajo': 0.3, 'medio': 0.5, 'alto': 0.2})
        rango_max = DiscreteDistribution({'bajo': 0.5, 'medio': 0.3, 'alto': 0.2})

        potencia = ConditionalProbabilityTable(
            [
                # Vida, Daño, Rango -> Potencia y su probabilidad
                ['bajo', 'bajo', 'bajo', 'bajo', 0.8],
                ['bajo', 'bajo', 'bajo', 'medio', 0.15],
                ['bajo', 'bajo', 'bajo', 'alto', 0.05],

                ['bajo', 'bajo', 'medio', 'bajo', 0.7],
                ['bajo', 'bajo', 'medio', 'medio', 0.2],
                ['bajo', 'bajo', 'medio', 'alto', 0.1],

                ['bajo', 'bajo', 'alto', 'bajo', 0.6],
                ['bajo', 'bajo', 'alto', 'medio', 0.3],
                ['bajo', 'bajo', 'alto', 'alto', 0.1],

                ['bajo', 'medio', 'bajo', 'bajo', 0.5],
                ['bajo', 'medio', 'bajo', 'medio', 0.3],
                ['bajo', 'medio', 'bajo', 'alto', 0.2],

                ['bajo', 'medio', 'medio', 'bajo', 0.4],
                ['bajo', 'medio', 'medio', 'medio', 0.4],
                ['bajo', 'medio', 'medio', 'alto', 0.2],

                ['bajo', 'medio', 'alto', 'bajo', 0.3],
                ['bajo', 'medio', 'alto', 'medio', 0.5],
                ['bajo', 'medio', 'alto', 'alto', 0.2],

                ['bajo', 'alto', 'bajo', 'bajo', 0.2],
                ['bajo', 'alto', 'bajo', 'medio', 0.4],
                ['bajo', 'alto', 'bajo', 'alto', 0.4],

                ['bajo', 'alto', 'medio', 'bajo', 0.1],
                ['bajo', 'alto', 'medio', 'medio', 0.5],
                ['bajo', 'alto', 'medio', 'alto', 0.4],

                ['bajo', 'alto', 'alto', 'bajo', 0.05],
                ['bajo', 'alto', 'alto', 'medio', 0.2],
                ['bajo', 'alto', 'alto', 'alto', 0.75],

                ['medio', 'bajo', 'bajo', 'bajo', 0.6],
                ['medio', 'bajo', 'bajo', 'medio', 0.3],
                ['medio', 'bajo', 'bajo', 'alto', 0.1],

                ['medio', 'bajo', 'medio', 'bajo', 0.5],
                ['medio', 'bajo', 'medio', 'medio', 0.4],
                ['medio', 'bajo', 'medio', 'alto', 0.1],

                ['medio', 'bajo', 'alto', 'bajo', 0.4],
                ['medio', 'bajo', 'alto', 'medio', 0.4],
                ['medio', 'bajo', 'alto', 'alto', 0.2],

                ['medio', 'medio', 'bajo', 'bajo', 0.4],
                ['medio', 'medio', 'bajo', 'medio', 0.4],
                ['medio', 'medio', 'bajo', 'alto', 0.2],

                ['medio', 'medio', 'medio', 'bajo', 0.3],
                ['medio', 'medio', 'medio', 'medio', 0.4],
                ['medio', 'medio', 'medio', 'alto', 0.3],

                ['medio', 'medio', 'alto', 'bajo', 0.2],
                ['medio', 'medio', 'alto', 'medio', 0.5],
                ['medio', 'medio', 'alto', 'alto', 0.3],

                ['medio', 'alto', 'bajo', 'bajo', 0.1],
                ['medio', 'alto', 'bajo', 'medio', 0.4],
                ['medio', 'alto', 'bajo', 'alto', 0.5],

                ['medio', 'alto', 'medio', 'bajo', 0.05],
                ['medio', 'alto', 'medio', 'medio', 0.5],
                ['medio', 'alto', 'medio', 'alto', 0.45],

                ['medio', 'alto', 'alto', 'bajo', 0.01],
                ['medio', 'alto', 'alto', 'medio', 0.2],
                ['medio', 'alto', 'alto', 'alto', 0.79],

                ['alto', 'bajo', 'bajo', 'bajo', 0.4],
                ['alto', 'bajo', 'bajo', 'medio', 0.4],
                ['alto', 'bajo', 'bajo', 'alto', 0.2],

                ['alto', 'bajo', 'medio', 'bajo', 0.3],
                ['alto', 'bajo', 'medio', 'medio', 0.5],
                ['alto', 'bajo', 'medio', 'alto', 0.2],

                ['alto', 'bajo', 'alto', 'bajo', 0.2],
                ['alto', 'bajo', 'alto', 'medio', 0.5],
                ['alto', 'bajo', 'alto', 'alto', 0.3],

                ['alto', 'medio', 'bajo', 'bajo', 0.3],
                ['alto', 'medio', 'bajo', 'medio', 0.4],
                ['alto', 'medio', 'bajo', 'alto', 0.3],

                ['alto', 'medio', 'medio', 'bajo', 0.2],
                ['alto', 'medio', 'medio', 'medio', 0.5],
                ['alto', 'medio', 'medio', 'alto', 0.3],

                ['alto', 'medio', 'alto', 'bajo', 0.1],
                ['alto', 'medio', 'alto', 'medio', 0.4],
                ['alto', 'medio', 'alto', 'alto', 0.5],

                ['alto', 'alto', 'bajo', 'bajo', 0.05],
                ['alto', 'alto', 'bajo', 'medio', 0.3],
                ['alto', 'alto', 'bajo', 'alto', 0.65],

                ['alto', 'alto', 'medio', 'bajo', 0.01],
                ['alto', 'alto', 'medio', 'medio', 0.2],
                ['alto', 'alto', 'medio', 'alto', 0.79],

                ['alto', 'alto', 'alto', 'bajo', 0.005],
                ['alto', 'alto', 'alto', 'medio', 0.1],
                ['alto', 'alto', 'alto', 'alto', 0.895],
            ],
            [vida_max, daño_max, rango_max]
        )


        desempeño_general = ConditionalProbabilityTable(
            [
                # Pmap, Meta -> Desempeño y su probabilidad
                ['bajo', 'bajo', 'bajo', 0.9],
                ['bajo', 'bajo', 'medio', 0.1],
                ['bajo', 'bajo', 'alto', 0.0],

                ['bajo', 'medio', 'bajo', 0.8],
                ['bajo', 'medio', 'medio', 0.15],
                ['bajo', 'medio', 'alto', 0.05],

                ['bajo', 'alto', 'bajo', 0.7],
                ['bajo', 'alto', 'medio', 0.2],
                ['bajo', 'alto', 'alto', 0.1],

                ['medio', 'bajo', 'bajo', 0.6],
                ['medio', 'bajo', 'medio', 0.3],
                ['medio', 'bajo', 'alto', 0.1],

                ['medio', 'medio', 'bajo', 0.5],
                ['medio', 'medio', 'medio', 0.4],
                ['medio', 'medio', 'alto', 0.1],

                ['medio', 'alto', 'bajo', 0.4],
                ['medio', 'alto', 'medio', 0.4],
                ['medio', 'alto', 'alto', 0.2],

                ['alto', 'bajo', 'bajo', 0.3],
                ['alto', 'bajo', 'medio', 0.5],
                ['alto', 'bajo', 'alto', 0.2],

                ['alto', 'medio', 'bajo', 0.2],
                ['alto', 'medio', 'medio', 0.5],
                ['alto', 'medio', 'alto', 0.3],

                ['alto', 'alto', 'bajo', 0.1],
                ['alto', 'alto', 'medio', 0.4],
                ['alto', 'alto', 'alto', 0.5],
            ],
            [meta, pmap]
        )


        mejor_personaje = ConditionalProbabilityTable(
            [
                # Desempeño General, Potencia -> Mejor Personaje y su probabilidad
                ['bajo', 'bajo', 'no', 0.9],
                ['bajo', 'bajo', 'si', 0.1],
                ['bajo', 'medio', 'no', 0.8],
                ['bajo', 'medio', 'si', 0.2],
                ['bajo', 'alto', 'no', 0.7],
                ['bajo', 'alto', 'si', 0.3],

                ['medio', 'bajo', 'no', 0.6],
                ['medio', 'bajo', 'si', 0.4],
                ['medio', 'medio', 'si', 0.7],
                ['medio', 'medio', 'no', 0.3],
                ['medio', 'alto', 'si', 0.85],
                ['medio', 'alto', 'no', 0.15],

                ['alto', 'bajo', 'no', 0.5],
                ['alto', 'bajo', 'si', 0.5],
                ['alto', 'medio', 'si', 0.8],
                ['alto', 'medio', 'no', 0.2],
                ['alto', 'alto', 'si', 0.95],
                ['alto', 'alto', 'no', 0.05],
            ],
            [desempeño_general, potencia]
        )

        meta_node = Node(meta, name="Meta")
        pmap_node = Node(pmap, name="Pmap")
        vida_max_node = Node(vida_max, name="Vida Max")
        daño_max_node = Node(daño_max, name="Daño Max")
        rango_max_node = Node(rango_max, name="Rango Max")
        potencia_node = Node(potencia, name="Potencia")
        desempeño_general_node = Node(desempeño_general, name="Desempeño General")
        mejor_personaje_node = Node(mejor_personaje, name="Mejor Personaje")

        self.model = BayesianNetwork("Selección del Mejor Personaje")
        self.model.add_states(meta_node, pmap_node, vida_max_node, daño_max_node, rango_max_node,
                              potencia_node, desempeño_general_node, mejor_personaje_node)
        self.model.add_edge(meta_node, desempeño_general_node)
        self.model.add_edge(pmap_node, desempeño_general_node)
        self.model.add_edge(vida_max_node, potencia_node)
        self.model.add_edge(daño_max_node, potencia_node)
        self.model.add_edge(rango_max_node, potencia_node)
        self.model.add_edge(potencia_node, mejor_personaje_node)
        self.model.add_edge(desempeño_general_node, mejor_personaje_node)
        self.model.bake()
    
    def graficar_red(self):
        # Crear el grafo
        grafo = nx.DiGraph()
        for nodo in self.model.states:
            grafo.add_node(nodo.name)
        for parent, child in self.model.edges:
            grafo.add_edge(parent.name, child.name)

        # Dibujar el grafo
        pos = nx.spring_layout(grafo)  # Layout de los nodos
        plt.figure(figsize=(10, 8))
        nx.draw(grafo, pos, with_labels=True, node_color="skyblue", node_size=3000, font_size=12, font_weight="bold", arrowsize=20)
        plt.title("Red Bayesiana: Selección del Mejor Personaje")
        plt.show()

    def predecir(self, entrada):
        return self.model.predict_proba(entrada)
