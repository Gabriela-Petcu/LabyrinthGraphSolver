def numeroteaza_noduri(matrice):
    noduri_numerotate = {}
    index = 0
    """
    Se numeroteaza nodurile din matricea de labirint si le mapeaza la un index unic
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:  
                noduri_numerotate[(i, j)] = index
                index += 1

    return noduri_numerotate

def matrice_adiacenta(graf, noduri_numerotate):
    numar_noduri = len(graf)
    """
    Creeaza o matrice de adiacenta pt graful dat pe baza nodurilor numerotate
    """
    matrice = [[0] * numar_noduri for _ in range(numar_noduri)]

    for coord, vecini in graf.items():
        index = noduri_numerotate[coord]
        for vecin in vecini:
            index_vecin = noduri_numerotate[vecin]
            matrice[index][index_vecin] = 1  

    return matrice
