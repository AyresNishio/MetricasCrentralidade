import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random as rd
from Rede.Rede import *
from funcGrafo import *
 
def dividir_rede(G):
    
    #1 Vertices distantes com maior excentricidade (b1 e b2)
    # Vertices de maior excentricidade
    max_exc = listar_maiores_exc(G)
    #Seleciona vertices distântes
    diametro = nx.diameter(G)
    barra1,barra2 = rd.sample(max_exc, 2)
    while(nx.shortest_path_length(G,barra1,barra2)!=diametro) : barra1,barra2 = rd.sample(max_exc, 2)

    print(barra1,barra2)



def listar_maiores_exc(G):
    exc = nx.eccentricity(G)
    diametro =max(exc.items())[1]
    max_exc = []
    for ex in exc.items():
        if(ex[1]==diametro): max_exc.append(ex[0])

    return max_exc

if __name__ == "__main__":

    nome_caso = 'med6b9m.txt'

    rede = Rede(nome_caso)

    G = montar_grafo_da_rede(rede)

    dividir_rede(G)

    #exibir_grafo_de_grupos(G, rede.coordenadas)
    #exibir_grafo_de_peso_de_medidas(G, rede.coordenadas)

    print("acabou")