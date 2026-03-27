# Sistema bancário - Módulo 1

nome = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')

saldo = 1500.70
print(f'Bem vindo, {nome}')
print(f'CPF: {cpf}')
print(f'Saldo atual: R${saldo:.2f}')

deps = float(input("Valor do depósito: "))
saldo = saldo + deps
print(f'Valor do depósito: R$ {deps}')

saque = float(input("Valor de saque:"))

if saque <=0:
    print("Valor inválido")
elif saque > saldo:
    print("Saldo Insuficiente")
else:
    saldo -= saque
    print(f'Saque de: R$ {saque}, saldo atualizado de R$: {saldo}')

if saldo <= 2000:
    print("Conta Básica")
elif saldo > 2000 and saldo <=50000:
    print("Conta Premium")
else:
    print("Conta Black")