class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muistin_koko = muistin_koko
        self._siirrot = []
        self._vapaa_muisti_indeksi = 0

    def aseta_siirto(self, siirto):
        self._siirrot.append(siirto)

        if len(self._siirrot) > self._muistin_koko:
            self._siirrot.pop(0)
    
    def anna_siirto(self):
        if len(self._siirrot) == 2:
            return "k"

        laskin = {"k": 0, "p": 0, "s": 0}

        for i in range(0, len(self._siirrot) - 1):
            laskin[self._siirrot[i]] += 1

        if laskin["k"] > laskin["p"] or laskin["k"] > laskin["s"]:
            return "p"
        elif laskin["p"] > laskin["k"] or laskin["p"] > laskin["s"]:
            return "s"
        else:
            return "k"