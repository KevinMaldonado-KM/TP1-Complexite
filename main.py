import time

# Exemple d'utilisation
graphe10 = {
    0: [1, 2, 3],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 5],
    3: [0, 1, 2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6],
    6: [3, 5],
    7: [4, 8],
    8: [7],
    9: [0, 8]
}

graphe20 = {
    0: [1, 2, 3, 4],
    1: [0, 2, 5],
    2: [0, 1, 6],
    3: [0, 7],
    4: [0, 8],
    5: [1, 6],
    6: [2, 5],
    7: [3, 8],
    8: [4, 7],
    9: [10, 11],
    10: [9, 12],
    11: [9, 12],
    12: [10, 11],
    13: [14, 15],
    14: [13, 16],
    15: [13, 16],
    16: [14, 15],
    17: [18, 19],
    18: [17, 19],
    19: [17, 18]
}

graphe30 = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2, 4],
    4: [3, 5],
    5: [4, 8],
    6: [3, 9],
    7: [10],
    8: [5, 11],
    9: [6, 12],
    10: [7, 13],
    11: [8, 14],
    12: [9, 15],
    13: [10, 16],
    14: [11, 17],
    15: [12, 18],
    16: [13, 19],
    17: [14, 20],
    18: [15, 21],
    19: [16, 22],
    20: [17, 23],
    21: [18, 24],
    22: [19, 25],
    23: [20, 26],
    24: [21, 27],
    25: [22, 28],
    26: [23, 29],
    27: [24],
    28: [25],
    29: [26]
}

sous_ensemble = [0, 1, 2]

#Choix du graphe
graphe = graphe30

# Question 1 - Test de verification
def est_zone_dense(graphe, sous_ensemble):
    for u in sous_ensemble:
        for v in sous_ensemble:
            if u != v and v not in graphe[u]:
                return False

    return True


# Question 2 - Calcul de zone dense maximale
def zone_dense_maximale(graphe, sommet_depart):
    zone_dense_max = [sommet_depart]
    liste_sommets = list(graphe.keys())

    for sommet in liste_sommets:
        if sommet != sommet_depart:
            if est_zone_dense(graphe, zone_dense_max + [sommet]):
                zone_dense_max.append(sommet)

    return zone_dense_max


# Question 3 - Calcul de zone dense maximum (méthode complète)

def combinaisons(sommets, k):
    if k == 0:
        return [[]]

    if not sommets:
        return []

    tete, queue = sommets[0], sommets[1:]
    avec_tete = [[tete] + c for c in combinaisons(queue, k - 1)]
    sans_tete = combinaisons(queue, k)

    return avec_tete + sans_tete


def zone_dense_maximum(graphe):
    sommets = list(graphe.keys())

    zone_dense_maximale = []

    for i in range(1, len(sommets) + 1):
        combinaisons_i = combinaisons(sommets, i)
        for combinaison in combinaisons_i:
            if est_zone_dense(graphe, combinaison):
                zone_dense_maximale = combinaison

    return zone_dense_maximale


# Question 4 - Calcul zone dense maximum (méthode incomplète)
def zone_dense_maximum_incomplete(graphe):

    sommets = list(graphe.keys())
    sommets.sort(key=lambda x: len(graphe[x]), reverse=True)

    zone_dense_max_sommets = []
    max_sommets = 0

    while sommets:
        sommet_courant = sommets.pop(0)
        ensemble_courant = {sommet_courant}

        for sommet in sommets[:]:
            if all(voisin in ensemble_courant for voisin in graphe[sommet]):
                ensemble_courant.add(sommet)
                sommets.remove(sommet)

        if est_zone_dense(graphe, ensemble_courant):
            nb_sommets = len(ensemble_courant)
            if nb_sommets > max_sommets:
                max_sommets = nb_sommets
                zone_dense_max_sommets = ensemble_courant

    return zone_dense_max_sommets


# Fonction pour calculer le temps d'exécution d'une fonction
def mesure_duree_execution(fonction, *args):
    debut = time.time()
    resultat = fonction(*args)
    fin = time.time()
    duree = (fin - debut) * 1000
    return resultat, duree


#Test Question 1
resultat, duree = mesure_duree_execution(est_zone_dense, graphe, sous_ensemble)
if resultat:
    print("Le sous-ensemble est une zone dense.")
else:
    print("Le sous-ensemble n'est pas une zone dense.")
print("Temps d'exécution de est_zone_dense:", duree)


#Test Question 2
sommet_depart = 7
resultat, duree = mesure_duree_execution(zone_dense_maximale, graphe, sommet_depart)
print("La plus grande zone dense à partir du sommet", sommet_depart, "est:", resultat)
print("Temps d'exécution de zone_dense_maximale (ms) :", duree)


#Test Question 3
resultat, duree = mesure_duree_execution(zone_dense_maximum, graphe)
if resultat:
    print("Zone dense maximum:", resultat)
else:
    print("Aucune zone dense maximum trouvée.")
print("Temps d'exécution de zone_dense_maximum (ms) :", duree)


#Test Question 4
resultat, duree = mesure_duree_execution(zone_dense_maximum_incomplete, graphe)
print("Zone dense maximum incomplète : ", resultat)
print("Temps d'exécution de zone_dense_maximum_incomplete (ms) :", duree)