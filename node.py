class Node:
    def __init__(self, coord):
        self.coord = coord  # coordonatele nodului
        self.vecini = []    # lista de vecini

    def adauga_vecin(self, vecin):
        self.vecini.append(vecin)  # adauga un nod vecin

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.coord == other.coord  # compara coordonatele
        return False

    def __hash__(self):
        return hash(self.coord)  # permite utilizarea nodului în seturi
