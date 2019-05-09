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


class NotaInvalid(ValueError):
    pass


def nota(text):
    valor = float(text)

    if valor < 0 or valor > 10:
        raise NotaInvalid('Nota entre 0 e 10.')

    return valor


def boletim():
    continuar = True

    while continuar:
        nome = entrada('Nome e Sobrenome: ')
        notas = [
            entrada('Primeira nota: ', nota),
            entrada('Segunda nota: ', nota),
            entrada('Terceira nota: ', nota),
        ]

        yield nome, notas

        continuar = entrada('Quer adicionar outro aluno? [S/n] ', SN)
