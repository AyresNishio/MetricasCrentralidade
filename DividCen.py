import numpy as np
import matplotlib.pyplot as plt
from System_Display_w import *


#monta grafo
med_plan = np.loadtxt('med118b333m.txt',dtype = 'i')
num_barras = 118

#Ybarra e coordenadas
coord, Ybus = coords(118) 
G  = Monta_sys(range(1,np.size(Ybus,0)+1),Ybus)

# Mostra Topologia da Rede
#Display_sys(G, coord,'black')
# Mostra Topologia de acordo com a 
#Display_sys(G,'fruchterman','black')
# Mostra Concentração das medidas
#display_w(G, med_plan,coord)

#1 Vertices distantes com maior escentricidade
escentricidades = eccentricity(G)
e = []
for barra, escentricidade in sorted(escentricidades.items(), key=lambda item: item[1]):
    print (f'{barra}: {escentricidade}')
    e.append([barra,escentricidade])

#Seleciona primeira barra com maior escentricidade
b1 = e[-1]
i = -2
while(nx.shortest_path_length(G,b1[0],e[i][0]) != b1[1]):
    i = i-1
#Seleciona barra com maior distância da primeira barra
b2 = e[i]
#2 Dividir rede

#3 Balanceamento

print('fim')