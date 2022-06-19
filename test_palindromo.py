import unittest
from palindromo import palindromo

class TestSum(unittest.TestCase):

    def test_pal1(self):
        self.assertEqual(palindromo.palindromo("r"), True, "Deveria ser verdadeiro")
    def test_pal2(self):
        self.assertEqual(palindromo.palindromo("Rotator"), True, "Deveria ser verdadeiro")
    def test_pal3(self):
        self.assertEqual(palindromo.palindromo("bob"), True, "Deveria ser verdadeiro")
    def test_pal4(self):
        self.assertEqual(palindromo.palindromo("madam"), True, "Deveria ser verdadeiro")
    def test_pal5(self):
        self.assertEqual(palindromo.palindromo("mAlAyAlam"), True, "Deveria ser verdadeiro")
    def test_pal6(self):
        self.assertEqual(palindromo.palindromo("1"), True, "Deveria ser verdadeiro")
    def test_pal7(self):
        self.assertEqual(palindromo.palindromo("Able was I, ere I saw Elba"), True, "Deveria ser verdadeiro")
    def test_pal8(self):
        self.assertEqual(palindromo.palindromo("Madam I’m Adam"), True, "Deveria ser verdadeiro")
    def test_pal9(self):
        self.assertEqual(palindromo.palindromo("Step on no pets."), True, "Deveria ser verdadeiro")
    def test_pal10(self):
        self.assertEqual(palindromo.palindromo("Top spot!"), True, "Deveria ser verdadeiro")
    def test_pal11(self):
        self.assertEqual(palindromo.palindromo("02/02/2020"), True, "Deveria ser verdadeiro")
    def test_pal12(self):
        self.assertEqual(palindromo.palindromo("Socorram-me subi no ônibus em marrocos"), True, "Deveria ser verdadeiro")
    def test_pal13(self):
        self.assertEqual(palindromo.palindromo("xyz"), False, "Deveria ser falso")
    def test_pal14(self):
        self.assertEqual(palindromo.palindromo("elephant"), False, "Deveria ser falso")
    def test_pal15(self):
        self.assertEqual(palindromo.palindromo("Country"), False, "Deveria ser falso")
    def test_pal16(self):
        self.assertEqual(palindromo.palindromo("Top . post!"), False, "Deveria ser falso")
    def test_pal17(self):
        self.assertEqual(palindromo.palindromo("Wonderful-fool"), False, "Deveria ser falso")
    def test_pal18(self):
        self.assertEqual(palindromo.palindromo("Wild imagination!"), False, "Deveria ser falso")
