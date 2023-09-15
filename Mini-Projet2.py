def est_relie_par_des_aretes(graphe, sous_ensemble):
    for u in sous_ensemble:
        for v in sous_ensemble:
            if u != v and v not in graphe[u]:
                return False
    return True

def est_zone_dense(graphe, sous_ensemble):
    return est_relie_par_des_aretes(graphe, sous_ensemble)

# Exemple d'utilisation
graphe = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

sous_ensemble = [0, 1, 2]
resultat = est_zone_dense(graphe, sous_ensemble)

if resultat:
    print("Le sous-ensemble est une zone dense.")
else:
    print("Le sous-ensemble n'est pas une zone dense.")

#Complexité O(X²)