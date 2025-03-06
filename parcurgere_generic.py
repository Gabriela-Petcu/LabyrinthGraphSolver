from collections import deque
from node import Node

def este_iesire(coord, matrice):
    """
    Verifica daca coordonatele specificate reprezinta o iesire din labirint. 
    """
    x, y = coord
    return x == 0 or x == len(matrice) - 1 or y == 0 or y == len(matrice[0]) - 1

def generic_program(graf, nod_start, noduri_numerotate, matrice):
    """
    -alg de parcurgere generica pentru a gasi toate drumurile dintr un labirint,
    identificand iesirile accesibile si inaccesibile;
    """
    coord_nod_start = nod_start.coord
    print(f"Începem parcurgerea de la nodul de start: {coord_nod_start}")

    drumuri = [] #lista pt a pastra drumurile gasite
    iesiri_accesibile = [] #lista pentru iesirile accesibile
    iesiri_inaccesibile = [] #lista pt iesirile inaccesibile
    coada = deque([(nod_start, [nod_start.coord])]) #coada pt parcurgere
    vizitate = set() #set pt a pastra nodurile vizitate

    while coada:
        """
        Pana cand coada va fi goala se extrage nodul curent si calea sa si se obtine 
        coordonatele nodului curent. 
        Se verifica daca nodul a fost deja vizitat si se trece la urmatorul daca da.
        Se marcheaza nodul curent ca vizitat.
        """
        current_node, path = coada.popleft()
        coord_current = current_node.coord
        print(f"Procesăm nodul: {coord_current}")

        if coord_current in vizitate:
            continue

        vizitate.add(coord_current)

        if este_iesire(coord_current, matrice):
            """
            Verif daca nodul curent este iesire. Adauga drumul la iesirile accesibile,
            adauga drumul curent la lista de drumuri.
            """
            iesiri_accesibile.append(path)
            print(f"Ieșire accesibilă găsită: {coord_current}, Drumul: {path}")
        else:
            drumuri.append(path)

        for vecin_coord in graf.get(coord_current, []):
            """
            Se parcurg vecinii nodului curent. Daca nu a fost vizitat, se adauga vecinul la coada.
            """
            if vecin_coord not in vizitate:
                coada.append((Node(vecin_coord), path + [vecin_coord]))

    # identificam iesirile inaccesibile
    for coord in graf.keys():
        """
        Se parcurg toate coordonatele din graf.
        Se verifica iesirile inaccesibile. 
        """
        if este_iesire(coord, matrice) and coord not in vizitate:
            iesiri_inaccesibile.append(coord)
            print(f"Ieșire inaccesibilă detectată: {coord}")

    return drumuri, iesiri_accesibile, iesiri_inaccesibile
