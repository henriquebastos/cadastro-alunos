from collections import namedtuple
from enum import Enum

from cadastro.input import boletim


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


def main():
    return [Aluno(nome, notas, avg(*notas), conceito(avg(*notas))) for nome, notas in boletim()]




