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
# Mostra Topologia da Rede
#Display_sys(G, coord,'black')
# Mostra Topologia de acordo com a 
#Display_sys(G,'fruchterman','black')
# Mostra Concentração das medidas
#display_w(G, med_plan,coord)

#1 Vertices distantes com maior excentricidade (b1 e b2)
excentricidades = eccentricity(G)
e = []
for barra, excentricidade in sorted(excentricidades.items(), key=lambda item: item[1]):
    #print (f'{barra}: {escentricidade}')
    e.append([barra,excentricidade])

#Seleciona primeira barra com maior escentricidade
b1 = e[-1]
i = -2
while(nx.shortest_path_length(G,b1[0],e[i][0]) != b1[1]):
    i = i-1

#Seleciona barra com maior distância da primeira barra
b2 = e[i]

#2 Dividir rede
# Vertices mais próximos de b1 são adicionados ao Grupo 1, vertices mais proximos de b2 são adicionados ao Grupo 2 
for barra in G.nodes():
    if(nx.shortest_path_length(G,b1[0],barra) < nx.shortest_path_length(G,b2[0],barra)): 
        G.nodes[barra]['grupo'] = 0
    else:
        G.nodes[barra]['grupo'] = 1

#Display_sys(G, coord,'black')
#Display_sys(G, 'fruchterman','black')

#3 Balanceamento

#Pesos iniciais
peso_grupo = [0,0]
for barra in G.nodes:
    if(G.nodes[barra]['grupo'] == 0): peso_grupo[0] = peso_grupo[0]+G.nodes[barra]['medidas']
    if(G.nodes[barra]['grupo'] == 1): peso_grupo[1] = peso_grupo[1]+G.nodes[barra]['medidas']
print(peso_grupo[0], peso_grupo[1])
for i in range(5):
    Display_sys(G, f_pos,'black')
    if( peso_grupo[0] < peso_grupo[1]):
        grupo_menor = 0
        grupo_maior = 1
    else:
        grupo_menor = 1
        grupo_maior = 0

    #Barras de fronteira.
    barras_fronteira = []
    for barra in G.nodes:
        fronteira = False
        for vizinho in G.neighbors(barra):
            if(G.nodes[barra]['grupo'] == grupo_maior and G.nodes[vizinho]['grupo'] != G.nodes[barra]['grupo']): 
                fronteira = True
        if (fronteira) : barras_fronteira.append(barra)
    #random.seed(10)
    desv_peso = np.abs(peso_grupo[0] - peso_grupo[1])
    barra_trocada = random.choice(barras_fronteira)
    G.nodes[barra_trocada]['grupo'] = grupo_menor
    peso_grupo[grupo_menor] = peso_grupo[grupo_menor] + G.nodes[barra_trocada]['medidas']
    peso_grupo[grupo_maior] = peso_grupo[grupo_maior] - G.nodes[barra_trocada]['medidas']
    novo_desv_peso = np.abs(peso_grupo[0] - peso_grupo[1])
    print(barra_trocada, novo_desv_peso, desv_peso)
    if(novo_desv_peso<=desv_peso): 
        desv_peso = novo_desv_peso
    else: 
        G.nodes[barra_trocada]['grupo'] = grupo_maior
        peso_grupo[grupo_menor] = peso_grupo[grupo_menor] - G.nodes[barra_trocada]['medidas']
        peso_grupo[grupo_maior] = peso_grupo[grupo_maior] + G.nodes[barra_trocada]['medidas']
    print(desv_peso)
    
peso_grupo = [0,0]
for barra in G.nodes:
    if(G.nodes[barra]['grupo'] == 0): peso_grupo[0] = peso_grupo[0]+G.nodes[barra]['medidas']
    if(G.nodes[barra]['grupo'] == 1): peso_grupo[1] = peso_grupo[1]+G.nodes[barra]['medidas']
print(peso_grupo[0], peso_grupo[1])

Display_sys(G, f_pos,'black')
print('fim')