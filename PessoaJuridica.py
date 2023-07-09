from Cliente import Cliente
from Endereco import Endereco
from datetime import datetime


class PessoaJuridica(Cliente): 
    def __init__(self, cnpj = None, razao_social = None, endereco = Endereco): 
        super().__init__(endereco)
        self._cnpj = cnpj
        self._razao_social = razao_social

    def __str__(self):
        return f"Pessoa Jurídica ->  Razão Social: {self._razao_social} CNPJ:{self._cnpj} Cliente desde: {self.data_cadastro.strftime('%d/%m/%Y')}"
    
    def mostrar_cadastro(self):
        detalhes_cadastro = f"""
    Dados cadastrais
    ----------------
    Data cadastro:      {self.data_cadastro.strftime('%d/%m/%Y')}
    C.N.P.J.:           {self._cnpj}
    Razão Social:       {self._razao_social}
    Endereço:           {self._endereco.obter_completo()}
        """
        print(detalhes_cadastro)

    def cadastrar(self, cnpj = None):
        if (not cnpj):
            self._cnpj = input("CNPJ: ")
        self._razao_social = input("Informe a razão social: ")
        endereco = Endereco()
        endereco.cadastrar() 
        self._endereco = endereco