listaAlunos = []
adicionar = ' '
notas = []
conceito = ''

while True:
    alunos = {'Nome': str(input('Nome e Sobrenome: ')).strip()}

    try:
        dados = float(input('Primeira nota: '))
    except ValueError:
        print('Entrada incorreta de dados.Tente Novamente')
        notas.clear()
        continue
    else:
        notas.append(dados)
    try:
        dados = float(input('Segunda nota: '))
    except ValueError:
        print('Entrada incorreta de dados.Tente novamente')
        notas.clear()
        continue
    else:
        notas.append(dados)
    try:
        dados = float(input('Terceira nota: '))
    except ValueError:
        print('Entrada incorreta de dados.Tente novamente')
        notas.clear()
        continue
    else:
        notas.append(dados)
        alunos['Notas'] = notas[:]

        alunos['Media'] = (notas[0] + notas[1] + notas[2]) / 3

        if alunos['Media'] <= 5:
            conceito = 'Ruin'
            alunos['Conceito'] = conceito

        elif alunos['Media'] <= 7:
            conceito = 'Bom'
            alunos['Conceito'] = conceito
        elif alunos['Media'] >= 8:
            conceito = 'Excelente'
            alunos['Conceito'] = conceito

            listaAlunos.append(alunos)

            adicionar = input('Quer adicionar outro aluno? [S/N] ').upper()


        if adicionar == 'N':
            break



        elif adicionar == 'S':
            notas.clear()
print(listaAlunos)
