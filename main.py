from citire_labirint import citire_labirint
from conversie_matrice import matrice_adiacenta, numeroteaza_noduri
from graf_labirint import transformare_in_graf
from parcurgere_generic import generic_program
from afisare_grafica import InterfataLabirint
from node import Node

def main():
    nume_fisier = r'D:\Facultate\Anul2Sem1\AG\teme\tema2AG\labirint.txt'
    matrice = citire_labirint(nume_fisier)

    noduri_numerotate = numeroteaza_noduri(matrice)
    print("Noduri numerotate:", noduri_numerotate)

    graf = transformare_in_graf(matrice, noduri_numerotate)
    matrice_adiacenta_neorientata = matrice_adiacenta(graf, noduri_numerotate)

    """
    Numerotarea nodurilor ajuta la identificarea poz valide din labirint pt parcurgere.
    Bucla while permita introducerea unei chei de nod de start si verifica daca e valida.
    Functia generic_program este responsabila pentru calcularea drumurilor si identificare iesirilor
    inaccesibile.
    """
    while True:
        try:
            cheia_nod_start = int(input("Introduceți cheia nodului de start: "))
            coord_nod_start = next(key for key, value in noduri_numerotate.items() if value == cheia_nod_start)
            break
        except ValueError:
            print("Te rog introdu un număr valid.")
        except StopIteration:
            print("Cheia introdusă nu există. Te rog introdu o cheie validă.")

    #se apeleaza functia de parcurgere generica pt drumurile si iesirile inaccesibile
    P, drumuri, iesiri_inaccesibile = generic_program(graf, Node(coord_nod_start), noduri_numerotate, matrice)

    # lansam interfata grafica, afisand iesirile inaccesibile
    interfata = InterfataLabirint(matrice, drumuri, coord_nod_start, iesiri_inaccesibile)
    interfata.run()

if __name__ == "__main__":
    main()
