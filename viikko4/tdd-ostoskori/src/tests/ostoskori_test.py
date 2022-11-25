import unittest
from ostoskori import Ostoskori
from tuote import Tuote

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

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_2_tavaraa_ja_hinta_oikein(self):
        water = Tuote("water", 1)
        self.kori.lisaa_tuote(water)
        self.kori.lisaa_tuote(water)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)