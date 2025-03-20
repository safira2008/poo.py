class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.marca} {self.modelo} está agora ligado.")
        else:
            print(f"O carro {self.marca} {self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"O carro {self.marca} {self.modelo} está agora desligado.")
        else:
            print(f"O carro {self.marca} {self.modelo} já está desligado.")

    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        estado = "ligado" if self.ligado else "desligado"
        print(f"Estado: {estado}")

# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla", 2020, "Preto")
meu_carro.mostrar_informacoes()
meu_carro.ligar()
meu_carro.desligar()