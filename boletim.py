alunos = int(input('Digite a quantidade de alunos:'))
boletim = ''

for aluno in range(0+ alunos):

    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))

    if(nota >= 7.5):
        boletim = boletim + 'O aluno ' + nome + ' passou de ano com nota ' + str(nota) + '.\n'
    elif(nota >= 5):
        boletim = boletim + 'O aluno ' + nome + ' fará prova de recuperação por tirar nota ' + str(nota) + '.\n'
    elif(nota >= 2.5):
        boletim = boletim + 'O aluno ' + nome + ' irá para o conselho de classe por tirar nota ' + str(nota) + '.\n'
    else:
        boletim = boletim + 'O aluno ' + nome + ' não passou de ano com nota ' + str(nota) + '.\n'
print('O boletim é:\n'+ boletim)
print('fim do boletim.')