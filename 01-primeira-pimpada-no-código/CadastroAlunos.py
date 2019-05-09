import sys
from collections import namedtuple
from unittest import TestCase, main as runtests
from enum import Enum
from pprint import pprint


Aluno = namedtuple('Aluno', 'nome notas media conceito')

class Conceito(Enum):
    BOM = 'Bom'
    RUIM = 'Ruim'
    EXCELENTE = 'Excelente'


def avg(*notas):
    return sum(notas)/len(notas)


def conceito(media):
    if media <= 5:
        valor = Conceito.RUIM
    elif media < 8:
        valor = Conceito.BOM
    else:
        valor = Conceito.EXCELENTE

    return valor


def entrada(enunciado, tipo=str):
    while True:
        valor = input(enunciado)
        valor = valor.strip()

        try:
            valor = tipo(valor)
        except ValueError as e:
            print('Entrada incorreta de dados. Tente novamente.')
        else:
            break

    return valor


class SNInvalid(ValueError):
    pass


def SN(text):
    if text in 'Ss':
        valor = True
    elif text in 'Nn':
        valor = False
    else:
        raise SNInvalid('Digite S ou N.')

    return valor


def main():
    l = list()

    continuar = True

    while continuar:
        nome = entrada('Nome e Sobrenome: ')
        notas = [
            entrada('Primeira nota: ', nota),
            entrada('Segunda nota: ', nota),
            entrada('Terceira nota: ', nota),
        ]
        media = avg(*notas)

        l.append(Aluno(nome, notas, media, conceito(media)))

        continuar = entrada('Quer adicionar outro aluno? [S/n] ', SN)

    return l


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


class NotaInvalid(ValueError):
    pass


def nota(text):
    valor = float(text)

    if valor < 0 or valor > 10:
        raise NotaInvalid('Nota entre 0 e 10.')

    return valor


if __name__ == '__main__':
    if sys.argv[-1] == 'test':
        sys.argv.pop()
        runtests()
    else:
        pprint(main())


