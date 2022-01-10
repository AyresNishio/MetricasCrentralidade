import numpy as np
import matplotlib.pyplot as plt
import random

from numpy.typing import _16Bit 
from System_Display import *

#Monta grafo
med_plan = np.loadtxt('med118b333m.txt',dtype = 'i')
num_barras = 118



#Ybarra e coordenadas
coord, Ybus = coords(118) 
G  = Monta_sys(range(1,np.size(Ybus,0)+1),Ybus,med_plan)

f_pos = nx.fruchterman_reingold_layout(G)

#1 Árvore Geradora
T = nx.minimum_spanning_tree(G)
t_pos = nx.fruchterman_reingold_layout(T)
Display_sys(T,coord,'black')
Display_sys(T,t_pos,'black')

#1.2 Encontrar Folhas distântes
n_grupos = 3
folhas = []
graus = dict(nx.degree(T))
graus_ord = []
for barra, grau in sorted(graus.items(), key=lambda item: item[1]):
    graus_ord.append([barra,grau])

folhas.append(graus_ord[0][0])
diametro = nx.diameter(G)
i=1
teste_diametro = True
while(len(folhas) < n_grupos):
    for f in folhas:
        #print(nx.shortest_path_length(G,f,graus_ord[i][0]))
        if(nx.shortest_path_length(G,f,graus_ord[i][0])<diametro/2):
            teste_diametro=False
        
    if(teste_diametro):folhas.append(graus_ord[i][0])
    i+=1
    teste_diametro=True



#3 Dividir a rede

for barra in G.nodes():
    folha_proxima = -1
    menor_distancia = diametro+1
    for folha in folhas:
        distancia = nx.shortest_path_length(G,folha,barra)
        if(distancia < menor_distancia):
            folha_proxima = folha
            menor_distancia = distancia

        
        G.nodes[barra]['grupo'] = folhas.index(folha_proxima)
#Display_sys(G,coord,'black')
#4 Balanceamento
peso_grupo = np.zeros(n_grupos, dtype='i')
for barra in G.nodes:
    grupo = G.nodes[barra]['grupo']
    peso_grupo[grupo] = peso_grupo[grupo]+G.nodes[barra]['medidas']
print(peso_grupo)
Display_sys(G, f_pos,'black')
for i in range(10):
    maior_grupo = np.argmax(peso_grupo)
    #identifica grupo mais leve    
    menor_grupo = np.argmin(peso_grupo)
    desv_peso = 0 
    for ji in range(n_grupos):
        desv_peso = desv_peso + np.abs(peso_grupo[ji]-111)
    print(peso_grupo)
    print(desv_peso, maior_grupo, menor_grupo)
    #Barras de fronteira.
    barras_fronteira = []
    for barra in G.nodes:
        #fronteira = False
        for vizinho in G.neighbors(barra):
            if(G.nodes[barra]['grupo'] == menor_grupo and G.nodes[vizinho]['grupo'] != G.nodes[barra]['grupo']): 
                barras_fronteira.append([vizinho,G.nodes[vizinho]['grupo']])
    #random.seed(10)
    if(barras_fronteira):
        barra_trocada = random.choice(barras_fronteira)
        G.nodes[barra_trocada[0]]['grupo'] = menor_grupo
        peso_grupo[menor_grupo] = peso_grupo[menor_grupo] + G.nodes[barra_trocada[0]]['medidas']
        peso_grupo[barra_trocada[1]] = peso_grupo[barra_trocada[1]] - G.nodes[barra_trocada[0]]['medidas']

        novo_desv_peso = 0 
        for ji in range(n_grupos):novo_desv_peso = novo_desv_peso + np.abs(peso_grupo[ji]-111 )

        print(barra_trocada[0], novo_desv_peso, desv_peso)
        if(novo_desv_peso<=desv_peso): 
            desv_peso = novo_desv_peso
        else: 
            G.nodes[barra_trocada[0]]['grupo'] = barra_trocada[1]
            peso_grupo[menor_grupo] = peso_grupo[menor_grupo] - G.nodes[barra_trocada[0]]['medidas']
            peso_grupo[barra_trocada[1]] = peso_grupo[barra_trocada[1]] + G.nodes[barra_trocada[0]]['medidas']
    print(desv_peso)
    
peso_grupo = np.zeros(n_grupos,dtype='i')
for barra in G.nodes:
    grupo = G.nodes[barra]['grupo']
    peso_grupo[grupo] = peso_grupo[grupo]+G.nodes[barra]['medidas']

print(peso_grupo)
Display_sys(G, f_pos,'black')
Display_sys(G, coord,'black')

print('fim')
