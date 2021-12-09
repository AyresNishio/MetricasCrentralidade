import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def InitMeasGraph(Zm,Ybus,meas):
    

    GraphOrder = np.size(Ybus, 0)


    for row in meas:
        From = row[1]
        To = row[2]
        if From != To and Ybus[From - 1, To - 1] == 1:
            Zm.add_edge(From, To, weight = 1, label = 'P' + str(From) + '-' + str(To))

    for row in meas:
        From = row[1]
        To = row[2]
        Type = row[4]

        if To == From and Type == 2:
            for Col in range(GraphOrder):
                if (From - 1) != Col and Ybus[From - 1][Col] == 1:
                    Zm.add_edge(From, Col + 1, weight = 1, label = 'P' + str(From))

    return Zm

def Display_medGraph(Zm,Ybus,coord):
    v_labels = {x: x for x in Zm.nodes}
    nx.draw_networkx_labels(Zm, coord, v_labels, font_size=11, font_color='w', font_family = "Tahoma", font_weight = "normal")
    nx.draw_networkx_nodes(Zm, coord, node_color = 'r', node_size = 300, alpha = 1)
    ax = plt.gca()
    med_lin = dict()
    for i in range(len(Ybus)):
        for j in range(i,len(Ybus)):
            if (Ybus[i][j]==1):
                key = str(i+1) + '-' +str(j+1)
                med_lin[key] = 0

    # for i in Zm.neighbors(0):
    #     key =  '0-' +str(i)
    #     med_lin[key] = 0
    # print(med_lin)

    curvatura = [0,.1,-.1,.2,-.2,.3,-.3,.4,-.4]

    for e in Zm.edges:
        if(e[0]<e[1]):
            key = str(e[0]) +'-' + str(e[1])
        elif ((e[0]>e[1])):
            key = str(e[1]) +'-' + str(e[0])
        
        ax.annotate("",
                    xy=coord[e[0]], xycoords='data',
                    xytext=coord[e[1]], textcoords='data',
                    arrowprops=dict(arrowstyle="-", color="0.5",
                                    shrinkA=5, shrinkB=5,
                                    patchA=None, patchB=None,
                                    connectionstyle=f'arc3,rad={curvatura[med_lin[key]]}'),
                    )
        #nx.draw_networkx_edges(Zm,coord,edgelist=[(e[0],e[1])], connectionstyle=f"arc3,rad={curvatura[med_lin[key]]}")
        med_lin[key] = 1 + med_lin[key]
    plt.show()