import networkx as nx

class Validador():
    def __init__(self):
        self.G = nx.DiGraph()

    def validar(self, ini, dest, vals):
        self.G.add_weighted_edges_from(vals)

        print('-- Resultado verificado -- ')
        print(nx.dijkstra_path(self.G, ini, dest))
        print('Custo: ',nx.dijkstra_path_length(self.G, ini, dest))