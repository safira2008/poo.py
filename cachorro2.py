class Cachorro:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100  # Energia inicial do cachorro

    def brincar(self):
        if self.energia >= 10:
            self.energia -= 10
            print(f"{self.nome} está brincando! Energia agora: {self.energia}")
        else:
            print(f"{self.nome} está muito cansado para brincar.")

    def descansar(self):
        self.energia += 20
        if self.energia > 100:
            self.energia = 100  # A energia não pode ultrapassar 100
        print(f"{self.nome} descansou! Energia agora: {self.energia}")

    def status(self):
        print(f"{self.nome} tem {self.energia} de energia.")

# Exemplo de uso
if __name__ == "__main__":
    meu_cachorro = Cachorro("Rex")

    meu_cachorro.status()
    meu_cachorro.brincar()
    meu_cachorro.brincar()
    meu_cachorro.descansar()
    meu_cachorro.status()