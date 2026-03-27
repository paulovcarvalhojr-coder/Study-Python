from Cadastro_clientes import pessoas
from models.cliente import Cliente


def verif_cpf (cpf):
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            return True
    return False


cliente_teste = Cliente("João", "983.904.874-04", "123456")

cta = input('Informe o número da conta: ')
user = None
for id in pessoas:
    if id['conta'] == cta:
        user = id
        break

if user is None:
    print('Usuário não encontrado!')
else:

    while True:
        print('\n1-saldo 2-depósito 3-saque 0-sair')
        op = input('Opção: ')
        if op == "1":
            print(f'Saldo atualizado: R$ {user["saldo"]:.2f}')
        elif op == "2":
            deposito = float(input('Informe o valor do depósito: R$ '))
            if deposito < 0:
                print('Depósito Inválido')
            else:
                user['saldo'] += deposito
                print(f'Depósito de R$: {deposito:.2f}, saldo atualizado de: R$: {user["saldo"]:.2f}')
        elif op == "3":
            saque = float(input('Informe o valor do saque: R$ '))
            if saque <= 0:
                print('Saque inválido')
            elif saque > user['saldo']:
                print('Saldo Insuficiente')
            else:
                user['saldo'] -= saque
                print(f'Saque efetuado de: R$ {saque:.2f}, saldo atualizado de: R$ {user["saldo"]:.2f}')
        elif op == "0":
            print("Software finalizado")
            break
        else:
            print("Opção Inválida")