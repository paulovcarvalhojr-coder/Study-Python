class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print(f'{self.name}, speak Latir')

class Gato(Animal):
    def speak(self):
        print(f'{self.name} speak Miau')

dog = Dog('Bob')
cat = Gato('Bily')

dog.speak()
cat.speak()
