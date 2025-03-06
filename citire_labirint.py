def citire_labirint(nume_fisier):
    try:
        with open(nume_fisier, 'r') as fisier:
            matrice = [list(map(int, linie.strip().split())) for linie in fisier]
            print(f"Labirint citit cu succes: {matrice}")
    except FileNotFoundError:
        print(f"Eroare: Fișierul {nume_fisier} nu a fost găsit.")
        return []
    return matrice
