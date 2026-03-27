lista = ['João', 'José', 'Francisco']
#lista.append('Igor')
person = {'nome': 'João', 'idade': 33, 'cidade': 'São Paulo'}
#print(person)
#print(person['nome'])
#lista.pop(2)
#print(lista)

person1 = {'nome': 'José', 'idade': 35, 'cidade': 'São Paulo'}
person2 = {'nome': 'Igor', 'idade': 36, 'cidade': 'São Paulo'}
lista_person = []
lista_person.append(person)
lista_person.append(person1)
lista_person.append(person2)


#print(lista_person[0]['nome'])
i = 1
for i in range(len(lista_person)):
     print(lista_person[i]['nome'])
lista_nome = []

for p in lista_person:
    #print(p['nome'])
    lista_nome.append(p['nome'])

print(lista_nome)


