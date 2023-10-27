a = int(input('Digite um número: '))
while True: # quando while True, o loop é infinito, porque sempre que verificar o valor será True
    b = int(input('Digite outro número: '))
    if(b == 0):
        print('O divisor não pode ser zero')
    else:
        break # break é um comando para sair de um loop
divisao = a / b
print('A divisão dos números é :', divisao)