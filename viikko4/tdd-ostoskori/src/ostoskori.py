from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        count = 0
        for ostos in self.ostokset():
            count += ostos.lukumaara()

        return count

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0

        for ostos in self.ostokset():
            hinta += ostos.tuote.hinta() * ostos.lukumaara()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() in self.ostoslista.keys():
            self.ostoslista[lisattava.nimi()].muuta_lukumaaraa(1) 
        else:
            uusi_ostos = Ostos(lisattava)
            self.ostoslista[uusi_ostos.tuotteen_nimi()] = uusi_ostos

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() in self.ostoslista.keys():
            self.ostoslista[poistettava.nimi()].muuta_lukumaaraa(-1)
            if self.ostoslista[poistettava.nimi()].lukumaara() == 0:
                del self.ostoslista[poistettava.nimi()]
                
    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self.ostoslista.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
