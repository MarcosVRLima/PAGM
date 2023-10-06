import networkx as nx
import matplotlib.pyplot as plt

from modules.binaryTree import ArvoreBinaria

# Defina uma função para criar um gráfico a partir de uma árvore binária
def create_binary_tree_graph(root):
    G = nx.Graph()
    add_nodes(G, root)
    add_edges(G, root)
    return G

# Adicione nós ao gráfico a partir de uma árvore binária
def add_nodes(G, node):
    if node is not None:
        G.add_node(node.valor)
        add_nodes(G, node.esquerda)
        add_nodes(G, node.direita)

# Adicione arestas ao gráfico a partir de uma árvore binária
def add_edges(G, node):
    if node is not None:
        if node.esquerda is not None:
            G.add_edge(node.valor, node.esquerda.valor)
        if node.direita is not None:
            G.add_edge(node.valor, node.direita.valor)
        add_edges(G, node.esquerda)
        add_edges(G, node.direita)

def prim(graph):
    """
    Algoritmo de Prim para encontrar a árvore geradora mínima (AGM) de um grafo.
    
    :param graph: Um grafo não direcionado e ponderado.
    :return: A AGM do grafo.
    """
    # Inicializa a AGM como um grafo vazio.
    agm = nx.Graph()

    agmBinaryTree = ArvoreBinaria()
    
    # Seleciona um vértice inicial arbitrário (pode ser qualquer um).
    start_node = list(graph.nodes())[0]
    
    # Lista de vértices visitados.
    visited_nodes = {start_node}
    
    # Enquanto não visitarmos todos os vértices do grafo.
    while len(visited_nodes) < len(graph.nodes()):
        # Inicializa a menor aresta como None.
        min_edge = None
        
        # Para cada vértice visitado.
        for node in visited_nodes:
            # Encontra a aresta de menor peso que conecta um vértice visitado a um não visitado.
            for neighbor in graph.neighbors(node):
                if neighbor not in visited_nodes:
                    edge_data = graph[node][neighbor]
                    if min_edge is None or edge_data['weight'] < min_edge['weight']:
                        min_edge = {'source': node, 'target': neighbor, 'weight': edge_data['weight']}
        
        # Adiciona a aresta de menor peso à AGM.
        agm.add_edge(min_edge['source'], min_edge['target'], weight=min_edge['weight'])
        # agmBinaryTree.inserir(min_edge['source'], min_edge['target'], min_edge['weight'])
        
        # Marca o vértice alvo como visitado.
        visited_nodes.add(min_edge['target'])

    # # Crie o gráfico a partir da árvore binária
    # grafo = create_binary_tree_graph(agmBinaryTree.raiz)

    # # Desenhe o gráfico usando Matplotlib
    # pos = nx.spring_layout(grafo)
    # nx.draw(grafo, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    # plt.title("Árvore Binária")
    # plt.show()
    
    return agm
