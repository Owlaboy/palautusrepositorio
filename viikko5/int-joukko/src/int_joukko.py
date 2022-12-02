KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.lukujono = []

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujono.append(n)
    
    def lisaa_listan_alkiot(self, lista):
        for num in lista:
            self.lisaa(num)

    def poista(self, n):
        if n in self.lukujono:
            kohta = self.lukujono.index(n) # siis luku löytyy tuosta kohdasta :D
            self.lukujono.pop(kohta)

    def mahtavuus(self):
        return len(self.lukujono)

    def to_int_list(self):
        return self.lukujono.copy()

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()

        new = a.to_int_list() + b.to_int_list()

        x.lisaa_listan_alkiot(new)

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for num in a_taulu:
            if num in b_taulu:
                y.lisaa(num)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for num in b_taulu:
            if num in a_taulu:
                a_taulu.remove(num)

        z.lisaa_listan_alkiot(a_taulu)

        return z

    def __str__(self):
        lukujono = self.to_int_list()
        bruh = "{" + ", ".join(map(str,lukujono)) + "}"
        return bruh
        
