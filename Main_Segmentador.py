from Rede.Rede import *
from funcGrafo import *
from funcDividRede import *
from funcSegmentaRede import *
 
if __name__ == "__main__":

    #nome_caso = 'med3b9m.txt'
    nome_caso = 'med14b33m.txt'
    #nome_caso = 'med118b333m.txt'

    rede = Rede(nome_caso)

    G = montar_grafo_da_rede(rede)

    #exibir_grafo_de_peso_de_medidas(G, rede.coordenadas)

    G = segmentar_rede_em_n_grupos_m_vezes(G,3,5)
    
    exibir_grafo_de_grupos(G, rede.coordenadas)

    print("acabou")