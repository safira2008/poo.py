class Cachorro:
    def __init__(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = False
        self.feliz = False

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado")

    def dormir(self):
        self.acordado = False
        print(f"{self.nome} está dormindo")

    def comer(self):
        selfcomida -= 1
        print(f"{self.nome} comeu")


cachorro1 = Cachorro("mel","bull dog", 2)
cachorro1.acordar()
