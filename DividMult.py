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
        print(nx.shortest_path_length(G,f,graus_ord[i][0]))
        if(nx.shortest_path_length(G,f,graus_ord[i][0])<diametro/2):
            teste_diametro=False
        
    if(teste_diametro):folhas.append(graus_ord[i][0])
    i+=1
    teste_diametro=True



#3 Dividir Grupos



#4 Balanceamento

print('fim')
