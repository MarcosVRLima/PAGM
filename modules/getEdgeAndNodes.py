def getEdgeAndNodes(nomeArquivo):
    # Crie um dicionário vazio para armazenar as informações
    grafo = {}

    # Nome do arquivo
    # nomeArquivo = './AGM/DMXA/dmxa0296.stp'

    with open(nomeArquivo, 'r') as arquivo:
        for linha in arquivo:
            if linha.strip().startswith("E "):
                _, no1, no2, peso = linha.strip().split(" ")

                if int(no1) in grafo:
                    grafo[int(no1)].append((int(no2), int(peso)))
                else:
                    grafo[int(no1)] = [(int(no2), int(peso))]

                if int(no2) in grafo:
                    grafo[int(no2)] = []

    return grafo
               
# Exemplo de como acessar o dicionário
# grafo = getEdgeAndNodes('./AGM/DMXA/dmxa0296.stp')

# print(f"{grafo}\n\n {len(grafo)}")

# edges = 0
# for no, arestas in grafo.items():
#     print(f"Nó {no}:")
#     for destino, peso in arestas:
#         print(f"    Aresta para {destino} com peso {peso}")
#         edges += 1

# print(edges)
