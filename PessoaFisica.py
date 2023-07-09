from Cliente import Cliente
from Endereco import Endereco
from datetime import datetime


class PessoaFisica(Cliente): 
    def __init__(self, cpf = None, nome = None, data_nascimento_dia = None, data_nascimento_mes = None, data_nascimento_ano = None, endereco = Endereco): 
        super().__init__(endereco)
        self._documento = cpf
        self._nome = nome
        self._data_nascimento = datetime.now
        if (data_nascimento_dia):
            self._data_nascimento = datetime(int(data_nascimento_ano), int(data_nascimento_mes), int(data_nascimento_dia))

    @property
    def documento(self):
        return self._documento; 

    @property
    def idade(self): 
        return 2023 - int(self._data_nascimento.year)

    def __str__(self):
        return f"Pessoa Física   ->  Nome: {self._nome} CPF:{self._documento} Idade: {self.idade} anos Cliente desde: {self.data_cadastro.strftime('%d/%m/%Y')}"
    
    def mostrar_cadastro(self):
        detalhes_cadastro = f"""
    Cliente
    ----------------
    Pessoa física
    Data cadastro:      {self.data_cadastro.strftime('%d/%m/%Y')}
    C.P.F.:             {self._documento}
    Nome:               {self._nome}
    Idade:              {self.idade}  
    Data nascimento:    {self._data_nascimento.strftime('%d/%m/%Y')}
    Endereço:           {self._endereco.obter_completo()}
    Anos como cliente:  {self.anos_desde_cadastro}
"""
        return detalhes_cadastro

    def cadastrar(self, cpf = None):
        if (not cpf):
            self._documento = input("CPF: ")
        self._nome = input("Nome: ")
        data_nascimento_dia = int(input("Informe o dia da data de nascimento: "))
        data_nascimento_mes = int(input("Informe o mês de nascimento: "))
        data_nascimento_ano = int(input("Informe o ano da data de nascimento: "))
        self._data_nascimento = datetime(data_nascimento_ano, data_nascimento_mes, data_nascimento_dia)
        endereco = Endereco()
        endereco.cadastrar() 
        self._endereco = endereco
