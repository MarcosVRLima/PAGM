from modules.getEdgeAndNodes import getEdgeAndNodes
from modules.primAlgorithm import prim

import matplotlib.pyplot as plt
import networkx as nx

def criar_grafo(dados):
    # Crie um objeto de grafo direcionado
    grafo = nx.DiGraph()

    # Adicione os nós e as conexões com os pesos ao grafo
    for no_pai, conexoes in dados.items():
        for conexao in conexoes:
            no_filho, peso = conexao
            grafo.add_edge(no_pai, no_filho, weight=peso)

    return grafo

grafo = criar_grafo(getEdgeAndNodes('./AGM/DMXA/dmxa0296.stp'))

agm = prim(grafo)

# print(grafo)

# # Defina a posição dos nós (opcional)
pos = nx.spring_layout(agm)

# # Desenhe o grafo
nx.draw(agm, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_color='black', font_weight='bold', arrows=True)

# # Exiba o gráfico
plt.show()

plt.savefig("agm.png")  # Salve o gráfico como um arquivo PNG
