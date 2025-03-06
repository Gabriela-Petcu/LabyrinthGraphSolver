from node import Node

def transformare_in_graf(matrice, noduri_numerotate):
    graf = {}
    
    """
    Se transforma matricea de labirint intr-un graf.
    Se parcurge fiecare coordonata din nodurile numerotate pt initializarea listei de vecini.
    Se parcurge din nou pentru a adauga vecinii.
    Se definesc posibilele coordonate ale vecinilo.
    Se verifica fiecare vecin posibil.
      -Daca vecinul este in nodurile numerotate si este accesibil in matrice,
      il adauga in lista de vecini a coorodnatei curente.
    """
    for coord in noduri_numerotate.keys():
        graf[coord] = []  

    for coord in noduri_numerotate.keys():
        x, y = coord
        vecini_posibil = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

        for vecin in vecini_posibil:
            if vecin in noduri_numerotate and matrice[vecin[0]][vecin[1]] == 1:
                graf[coord].append(vecin) 

    return graf

