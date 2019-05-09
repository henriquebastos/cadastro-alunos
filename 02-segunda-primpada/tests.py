from unittest import TestCase

from cadastro.core import avg, conceito, Conceito, SN, NotaInvalid, nota


class TestMedia(TestCase):
    def test_media(self):
        self.assertEqual(avg(0, 10, 5.6), 5.2)


class TestConceito(TestCase):
    def test_conteito_0_ruin(self):
        self.assertEqual(conceito(0), Conceito.RUIM)

    def test_conceito_5_ruin(self):
        self.assertEqual(conceito(5), Conceito.RUIM)

    def test_conceito_5p1_media(self):
        self.assertEqual(conceito(5.1), Conceito.BOM)

    def test_conceito_7_media(self):
        self.assertEqual(conceito(7), Conceito.BOM)

    def test_conceito_7p9_media(self):
        self.assertEqual(conceito(7.9), Conceito.BOM)

    def test_conceito_8_excelente(self):
        self.assertEqual(conceito(8), Conceito.EXCELENTE)


class TestSN(TestCase):
    def test_sn_s(self):
        self.assertTrue(SN('S'))
        self.assertTrue(SN('s'))

    def test_sn_n(self):
        self.assertFalse(SN('N'))
        self.assertFalse(SN('n'))

    def test_sn_invalid(self):
        with self.assertRaises(ValueError):
            SN('invalid')


class TestNota(TestCase):
    def test_nota_menor_zero(self):
        with self.assertRaises(NotaInvalid):
            nota('-1')

    def test_nota_maior_dez(self):
        with self.assertRaises(NotaInvalid):
            nota('10.1')

    def test_nota_zero(self):
        self.assertEqual(nota(0), 0.0)

    def test_nota_dez(self):
        self.assertEqual(nota(10), 10.0)

