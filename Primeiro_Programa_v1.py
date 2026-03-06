nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')

saldo = 1500.70
print(f'Bem vindo, {nome}')
print(f'CPF: {cpf}')
print(f'Saldo atual: R${saldo:.2f}')

while True:
    print('\n1-saldo 2-depósito 3-saque 0-sair')
    op = input('Opção: ')
    if op == "0":
        print("Software finalizado")
        break
