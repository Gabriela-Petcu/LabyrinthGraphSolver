import tkinter as tk

class InterfataLabirint:
    def __init__(self, matrice, drumuri, intrare, iesiri_inaccesibile):
        self.root = tk.Tk() #fereastra principala
        self.matrice = matrice #stocheaza matricea labirintului
        self.drumuri = drumuri  #stocheaza drumurile identificate
        self.intrare = intrare #stocheaza coordonatele punctului de intrare
        self.iesiri_inaccesibile = iesiri_inaccesibile  # stocheaza iesirile inaccesibile
        self.canvas = tk.Canvas(self.root, width=300, height=300) #creeaza un canvas pt desenarea labirintului
        self.canvas.pack() #adauga canvas-ul in fereastra principala
        self.index_drum = 0 #indexul pentru a urmari drumul curent
        
        # buton pentru a afisa drumurile consecutiv
        buton_next = tk.Button(self.root, text="Next", command=self.afisare_urmator_drum)
        buton_next.pack()

        # deseneaza labirintul initial
        self.afiseaza_labirint()

    def afiseaza_labirint(self):
        """
        Deseneaza labirintul initial: pereti, cai accesibile și punct de intrare.
        """
        linii, coloane = len(self.matrice), len(self.matrice[0])
        cell_size = 30  # dimensiunea celulei în pixeli

        for i in range(linii):
            for j in range(coloane):
                x1, y1 = j * cell_size, i * cell_size #coordonatele coltului stanga sus
                x2, y2 = x1 + cell_size, y1 + cell_size #coordonatele coltului din dreapta jos
                
                if self.matrice[i][j] == 0:  # zid
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black") #zid negru
                elif self.matrice[i][j] == 1:  # cale accesibila
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")  #cale alb

        # punctul de intrare marcat cu albastru
        x1, y1 = self.intrare[1] * cell_size, self.intrare[0] * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    def afisare_urmator_drum(self):
        """
        Afiseaza urmatorul drum consecutiv cu verde, iar la final marchează ieșirile inaccesibile cu roșu.
        """
        if self.index_drum < len(self.drumuri):
            if self.index_drum > 0:  # daca nu este primul drum, recoloreaza drumul anterior
                self.repaint(self.drumuri[self.index_drum - 1])  # recoloreaza drumul anterior in alb

            drum = self.drumuri[self.index_drum] #obtine drumul curent
            self.coloreaza_drum(drum, "green")  # coloreaza drumul curent în verde
            self.index_drum += 1
        else:
            print("Nu mai sunt drumuri de afișat.")
            # coloreaza iesirile inaccesibile cu rosu
            for iesire in self.iesiri_inaccesibile:
                self.coloreaza_drum([iesire], "red")
                print(f"Ieșire inaccesibilă: {iesire}")

    def coloreaza_drum(self, drum, culoare):
        """
        Coloreaza drumul specificat cu culoarea dată.
        """
        cell_size = 30
        for (i, j) in drum:  #se parcurge fiecare coordonata din drumul specificat
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=culoare)

    def repaint(self, drum):
        """
        Recoloreaza drumul specificat în alb .
        """
        self.coloreaza_drum(drum, "white")  

    def run(self):
        """
        Rulează interfața grafică.
        """
        self.root.mainloop()
