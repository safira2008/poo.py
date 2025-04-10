class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def emitir_som(self):
        print(f"{self.nome} está fazendo um som...")

    def apresentar(self):
        print(f"Olá! Eu sou {self.nome}, um(a) {self.especie} de {self.idade} anos.")

    def envelhecer(self):
        self.idade += 1
        print(f"{self.nome} agora tem {self.idade} anos.")

# Criando objetos da classe Animal
animal1 = Animal("Toby", "Cachorro", 5)
animal2 = Animal("Mimi", "Gato", 3)

# Usando os métodos
animal1.apresentar()
animal1.emitir_som()
animal1.envelhecer()

print()  # só pra separar a saída

animal2.apresentar()
animal2.emitir_som()
animal2.envelhecer()
