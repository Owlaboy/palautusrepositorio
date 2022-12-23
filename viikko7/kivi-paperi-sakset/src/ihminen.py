class Ihminen:
    def __init__(self, first: bool = True):
        if first:
            self.message = "Ensinmäisen pelaajan siirto: "
        else:
            self.message = "Toisen pelaajan siirto: "

    def anna_siirto(self):
        return input(self.message)