class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.vanha = tulos

class Erotus():
    def __init__(self, tulos,io):
        self.tulos = tulos
        self.io = io

    def suorita(self):
        self.tulos.vanha = self.tulos.tulos
        self.tulos.tulos -= int(self.io())

    def kumoa(self):
        Kumoa(self.tulos)

class Summa():
    def __init__(self, tulos, io):
        self.tulos = tulos
        self.io = io

    def suorita(self):
        self.tulos.vanha = self.tulos.tulos
        self.tulos.tulos += int(self.io())
    
    def kumoa(self):
        Kumoa(self.tulos)

class Nollaa():
    def __init__(self, tulos, io):
        self.tulos = tulos

    def suorita(self):
        self.tulos.vanha = self.tulos.tulos
        self.tulos.tulos = 0 
    
    def kumoa(self):
        Kumoa(self.tulos)

class Kumoa():
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.tulos = self.sovelluslogiikka.vanha
