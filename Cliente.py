from Endereco import Endereco
from datetime import datetime


class Cliente:
    
    def __init__(self, endereco = Endereco()):
        self._data_cadastro = datetime.now()
        self._endereco = endereco 

    @property
    def data_cadastro(self): 
        return self._data_cadastro

    @data_cadastro.setter
    def data_cadastro(self, value ):
        self._data_cadastro = value

    @property
    def anos_desde_cadastro(self):
        data_atual = datetime.now()
        return data_atual.year - self.data_cadastro.year    
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
 