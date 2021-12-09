import numpy as np
import matplotlib.pyplot as plt
from System_Display_w import *


#monta grafo
med_plan = np.loadtxt('med118b333m.txt',dtype = 'i')
num_barras = 118

#Ybarra e coordenadas
coord, Ybus = coords(118) 
G  = Monta_sys(range(1,np.size(Ybus,0)+1),Ybus)

Display_sys(G, coord,'black')

display_w(G, med_plan,coord)

#1 Vertices distantes com maior centralidade

#2 Dividir rede

#3 Balanceamento