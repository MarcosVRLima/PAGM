import os
import tracemalloc
import time as t
import networkx as nx
import numpy as np

from modules.getEdgeAndNodes import getEdgeAndNodes
from modules.primsAlgorithm import prim
from modules.getArchives import listar_arquivos_em_pasta
from modules.report import report

def criar_grafo(dados):
    # Crie um objeto de grafo direcionado
    grafo = nx.Graph()

    # Adicione os nós e as conexões com os pesos ao grafo
    for no_pai, conexoes in dados.items():
        for conexao in conexoes:
            no_filho, peso = conexao
            grafo.add_edge(no_pai, no_filho, weight=peso)

    return grafo

def meansure():
    archives = listar_arquivos_em_pasta('./AGM/')
    for archive in archives:
        memoryPeaks = []
        timeExecutions = []
        for _ in range(10):
            grafo = criar_grafo(getEdgeAndNodes(archive))
            tracemalloc.start()
        
            time = t.perf_counter()
        
            agm = prim(grafo)

            time = t.perf_counter() - time

            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
        
            timeExecutions.append(time)
            memoryPeaks.append(peak)

        data = {
            "Nome da instancia": os.path.basename(archive),
            "Tempo médio (s)": np.mean(timeExecutions),
            "Tempo máximo (s)": np.max(timeExecutions),
            "Tempo mínimo (s)": np.min(timeExecutions),
            "Memória média (bytes)": float(np.mean(memoryPeaks)),
            "Memória máxima (bytes)": np.max(memoryPeaks),
            "Memória mínima (bytes)": np.min(memoryPeaks)
        }
        
        report(data)
    
    print(f"Arquivo {os.path.basename(archive)} terminado.")


