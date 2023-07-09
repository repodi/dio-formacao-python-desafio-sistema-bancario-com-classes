from Conta import Conta
from Saque import Saque


LIMITE_SAQUES = 3
LIMITE = 500

class ContaCorrente(Conta): 
    
    def __init__(self, numero, cliente, limite = LIMITE, limite_saques = LIMITE_SAQUES):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    @property
    def limite(self): 
        return self._limite
    
    @property
    def limite_saques(self): 
        return self._limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False
    