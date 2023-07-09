from Cliente import Cliente
from Historico import Historico

AGENCIA = "0001"

class Conta: 
   
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = AGENCIA
        self._cliente = cliente
        self._historico = Historico ()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)

    def __str__(self):
        return f"Agência: {self._agencia} Conta: {self._numero} {self._cliente}"

    def mostrar_cadastro(self):
        detalhes_cadastro = f"""
    Conta
    ----------------
    Agência:           {self._agencia}
    Número:            {self._numero}
"""        
        detalhe_cadastro_cliente = self._cliente.mostrar_cadastro()
        detalhes_cadastro += detalhe_cadastro_cliente
        print(detalhes_cadastro)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def listar_transacoes(self):
        for transacao in self.historico.transacoes:
            print(transacao)
        
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True
    