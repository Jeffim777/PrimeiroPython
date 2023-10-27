nota = float(input('Digite a nota do aluno: '))

if(nota >= 7):
    print('O aluno passou de ano.')
elif(nota >= 5):
    print('O aluno fará prova de recuperação.')
elif(nota >= 3):
    print('O aluno irá para o conselho de classe.')
else:
    print('O aluno não passou de ano.')

print('Análise concluída.')