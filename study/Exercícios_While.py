num = int(input('Digite um número: '))
contador = 0

while True:
    if num != 0:
        contador += num
        print(f'O número agora é: {contador}')
        num = int(input('Digite um número: '))
    else:
        print('Finalizado')
        break