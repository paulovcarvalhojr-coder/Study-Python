class Dog:
    def __init__(self, name: str):
        self.name = name
    def latir(self):
        print(f'{self.name} está latindo.')

dog1 = Dog('Bob')
dog2 = Dog('Rex')
dog3 = Dog('Pipito')

lista = [dog1, dog2, dog3]
for cach in lista:
    cach.latir()
