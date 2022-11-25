import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisayksen_jalkeen_korin_hinta_oikein(self):
        maito = Tuote("maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        truffel_oil = Tuote("truffle oil" , 99999)
        water = Tuote("water", 1)
        self.kori.lisaa_tuote(truffel_oil)
        self.kori.lisaa_tuote(water)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa(self):
        water = Tuote("water", 1)
        self.kori.lisaa_tuote(water)
        self.kori.lisaa_tuote(water)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_on_sama_kuin_2_kertaa_tuotteen_hinta(self):
        water = Tuote("fiji water", 50)
        self.kori.lisaa_tuote(water)
        self.kori.lisaa_tuote(water)

        self.assertEqual(self.kori.hinta(), 50*2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_1_ostos(self):
        water = Tuote("fiji water", 50)
        self.kori.lisaa_tuote(water)
        maara = len(self.kori.ostokset())

        self.assertEqual(maara, 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_oikean_ostoksen(self):
        water = Tuote("fiji water", 50)
        self.kori.lisaa_tuote(water)

        self.assertEqual(self.kori.ostokset()[0].tuote, water)

    def test_kahden_tuottee_lisaamisen_jalkeen_ostoskori_sisataa_kaksi_ostosta(self):
        water = Tuote("fiji water", 50)
        truffel_oil = Tuote("truffle oil" , 99999)
        self.kori.lisaa_tuote(water)
        self.kori.lisaa_tuote(truffel_oil)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        water = Tuote("fiji water", 50)
        self.kori.lisaa_tuote(water)
        self.kori.lisaa_tuote(water)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_oikean_laisen_ostoksen(self):
        water = Tuote("fiji water", 50)
        
        self.kori.lisaa_tuote(water)
        self.kori.lisaa_tuote(water)

        self.assertEqual(self.kori.ostokset()[0].tuotteen_nimi(), "fiji water")
        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_poistettua_yksi_tuote_ostoskori_sisaltaa_yhden_ostoksen(self):
        water = Tuote("fiji water", 50)
        self.kori.lisaa_tuote(water)
        self.kori.lisaa_tuote(water)
        self.kori.poista_tuote(water)

        self.assertEqual(self.kori.ostokset()[0].lukumaara(), 1)

    def test_viimeisen_tuotteen_poistamisen_jalkeen_korissa_on_0_ostosta(self):
        water = Tuote("fiji water", 50)
        self.kori.lisaa_tuote(water)
        self.kori.poista_tuote(water)

        self.assertEqual(len(self.kori.ostokset()), 0)
