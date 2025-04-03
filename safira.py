class ContaBancaria:
    def __init__(self, titular, limite):
        self.titular = titular
        self.saldo = 0.0
        self.limite = limite
        self.publica = False  # Conta é privada por padrão

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}')
        else:
            print('Valor de depósito deve ser positivo!')

    def sacar(self, valor):
        if valor > 0 and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}')
        else:
            print('Saque não permitido! Verifique o valor e seu limite.')

    def mudar_privacidade(self):
        self.publica = not self.publica
        estado = 'pública' if self.publica else 'privada'
        print(f'A conta agora é {estado}.')

    def mostrar_informacoes(self):
        estado = 'pública' if self.publica else 'privada'
        print(f'Titular: {self.titular}\nSaldo: R${self.saldo:.2f}\nLimite: R${self.limite:.2f}\nEstado: {estado}')

# Exemplo de uso
conta = ContaBancaria('João', 500.0)
conta.mostrar_informacoes()
conta.depositar(1000)
conta.sacar(1200)
conta.mudar_privacidade()
conta.mostrar_informacoes()

    
