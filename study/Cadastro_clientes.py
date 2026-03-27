pessoas = [
    {"nome": "Ana Souza", "data_nascimento": "12/05/1995", "idade": 30, "pais": "Brasil", 'cpf': '98390487402', "conta": "87402", "saldo": 0.00 },
    {"nome": "John Smith", "data_nascimento": "20/11/1988", "idade": 37, "pais": "EUA", 'cpf': '87694803943', "conta": "03943", "saldo": 0.00},
    {"nome": "Marie Curie", "data_nascimento": "03/02/2001", "idade": 25, "pais": "França", 'cpf': '67404850949', "conta": "50949", "saldo": 0.00},
    {"nome": "Carlos Ruiz", "data_nascimento": "15/07/1992", "idade": 33, "pais": "México", 'cpf': '98390487401', "conta": "87401", "saldo": 0.00},
    {"nome": "Elena Rossi", "data_nascimento": "30/09/1998", "idade": 27, "pais": "Itália", 'cpf': '98390487404', "conta": "87404", "saldo": 0.00}
]
def verif_cpf (cpf):
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            return True
    return False

while True:
    print('\n1-Adicionar novo usuário 2-Acessar banco')
    operacao = input('Digite a operação a ser efetuada: ')

    if operacao == "1":
        while True:
            print('\n1-adicionar 2-alterar 3-deletar 4-buscar 5-buscar_todos 0-sair')
            op = input('Opção: ')
            if op == "1":
                nome = input('Digite Nome: ')
                dt_nas = input('Digite a data de nascimento (no formato dd/mm/aaaa: ')
                id = int(input('Digite sua idade:'))
                pais = input('Digite o país: ')
                cpf = input('Digite seu CPF: ')
                if len(cpf) != 11:
                    print('Número de dígitos inválidos (11)')
                    continue
                if verif_cpf(cpf):
                        print('Faça um novo cadastro com CPF diferente')
                        continue
                else:
                    pessoa = {'nome': nome, 'data_nascimento': dt_nas, 'idade': id, 'pais': pais, 'cpf':cpf }
                    pessoas.append(pessoa)
                    print(f'Cadastrado com sucesso.{pessoa}')
            elif op == '2':
                cpf_busca = input('Digite o CPF de alteração: ')
                existe = False
                for pessoa in pessoas:
                    if pessoa['cpf'] == cpf_busca:
                        pais_novo = input('Informe o novo país: ')
                        idade_nova = int(input('Informa a nova idade: '))
                        pessoa['pais'] = pais_novo
                        pessoa['idade'] = idade_nova
                        existe = True
                        break
                if not existe:
                    print('CPF não encontrado')
            elif op == '3':
                cpf_busca = input('Digite o CPF para exclusão: ')
                for pessoa in pessoas:
                    if pessoa['cpf'] == cpf_busca:
                        pessoas.remove(pessoa)
                        break
            elif op == "4":
                cpf_busca = input('Digite o CPF de busca: ')
                for pessoa in pessoas:
                    if pessoa['cpf'] == cpf_busca:
                        print(pessoa)
                        break
            elif op == "5":
                for pessoa in pessoas:
                    print(f'Nome: {pessoa["nome"]}, CPF: {pessoa["cpf"]}')
            elif op == "0":
                    print("Software finalizado")
                    break
            else:
                print("Opção Inválida")



    else:
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



#criar função para as ações.







