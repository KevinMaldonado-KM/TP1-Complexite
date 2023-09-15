import networkx as nx

def creer_graphe():

    graphe_fixe = nx.Graph()

    noeuds = [0, 1, 2, 3, 4]
    graphe_fixe.add_nodes_from(noeuds)

    aretes = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 0)]
    graphe_fixe.add_edges_from(aretes)

    return graphe_fixe
'''
def liste_adjacence(graphe):
    
    liste_adj = {}
    for noeud in graphe.nodes():
        voisins = list(graphe.neighbors(noeud))
        liste_adj[noeud] = voisins
    return liste_adj
'''

graphe = creer_graphe()

'''
liste_d_adjacence = liste_adjacence(graphe)
print(liste_d_adjacence)
'''

sous_ensemble_de_noeuds = (0, 1, 2)
sous_graphe = graphe.subgraph(sous_ensemble_de_noeuds)

#Algo Question 1
def verif_zone_dense (sous_graphe):

    if (nx.density(sous_graphe) == 1):
        return True
    else:
        return False

print(verif_zone_dense(sous_graphe))