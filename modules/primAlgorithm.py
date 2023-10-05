import networkx as nx

def prim(graph):
    """
    Algoritmo de Prim para encontrar a árvore geradora mínima (AGM) de um grafo.
    
    :param graph: Um grafo não direcionado e ponderado.
    :return: A AGM do grafo.
    """
    # Inicializa a AGM como um grafo vazio.
    agm = nx.Graph()
    
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
        
        # Marca o vértice alvo como visitado.
        visited_nodes.add(min_edge['target'])
    
    return agm
