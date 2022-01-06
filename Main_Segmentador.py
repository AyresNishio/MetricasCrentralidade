from Rede.Rede import *
from funcGrafo import *
from funcDividRede import *
from funcSegmentaRede import *
 
if __name__ == "__main__":

    nome_caso = 'med6b9m.txt'

    rede = Rede(nome_caso)

    G = montar_grafo_da_rede(rede)

    G = segmentar_rede(G,3)

    exibir_grafo_de_grupos(G, rede.coordenadas)

    #exibir_grafo_de_peso_de_medidas(G, rede.coordenadas)

    print("acabou")