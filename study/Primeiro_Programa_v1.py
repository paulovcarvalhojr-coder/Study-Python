nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')

saldo = 1500.70
print(f'Bem vindo, {nome}')
print(f'CPF: {cpf}')
print(f'Saldo atual: R${saldo:.2f}')

while True:
    print('\n1-saldo 2-depósito 3-saque 0-sair')
    op = input('Opção: ')
    if op == "1":
        print(f'Saldo atualizado: R$ {saldo:.2f}')
    elif op == "2":
        deposito = float(input('Informe o valor do depósito: R$ '))
        if deposito < 0:
            print('Depósito Inválido')
        else:
            saldo += deposito
            print(f'Depósito de R$: {deposito:.2f}, saldo atualizado de: R$: {saldo:.2f}')
    elif op == "3":
        saque = float(input('Informe o valor do saque: R$ '))
        if saque <=0:
            print('Saque inválido')
        elif saque > saldo:
            print('Saldo Insuficiente')
        else:
            saldo -= saque
            print(f'Saque efetuado de: R$ {saque:.2f}, saldo atualizado de: R$ {saldo:.2f}')
    elif op == "0":
        print("Software finalizado")
        break
    else:
        print("Opção Inválida")

