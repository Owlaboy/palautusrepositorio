from tuomari import Tuomari
from ihminen import Ihminen
from tekoaly import Tekoaly
from parannettu_tekoaly import TekoalyParannettu

class KPSPeli:
    def __init__(self):
        self.pelaaja1 = None
        self.pelaaja2 = None
        self.tuomari = Tuomari()

    def ihminen(self):
        if not self.pelaaja1:
            self.pelaaja1 = Ihminen()
        else:
            self.pelaaja2 = Ihminen()
        return self

    def tekoaly(self):
        self.pelaaja2 = Tekoaly()
        return self

    def parannettutekoaly(self):
        self.pelaaja2 = TekoalyParannettu(20)
        return self

    def pelaa(self):
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")

        siirto1 = self.pelaaja1.anna_siirto()
        siirto2 = self.pelaaja2.anna_siirto()

        while self._laillinen_siirto(siirto1) and self._laillinen_siirto(siirto2):
            if self.pelaaja2.__class__.__name__ == "TekoalyParannettu":
                self.pelaaja2.aseta_siirto(siirto1)
            
            if self.pelaaja2.__class__.__name__ == "Tekoaly" or self.pelaaja2.__class__.__name__ == "TekoalyParannettu":
                print(f"Tietokone valitsi: {siirto2}")

            self.tuomari.kirjaa_siirto(siirto1, siirto2)
            print(self.tuomari)

            siirto1 = self.pelaaja1.anna_siirto()
            siirto2 = self.pelaaja2.anna_siirto()
        
        print("kiitos!")
        
    def _laillinen_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"



    