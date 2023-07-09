from Cliente import Cliente
from Endereco import Endereco
from datetime import datetime


class PessoaJuridica(Cliente): 
    def __init__(self, cnpj = None, razao_social = None, endereco = Endereco): 
        super().__init__(endereco)
        self._documento = cnpj
        self._razao_social = razao_social

    @property
    def documento(self):
        return self._documento

    def __str__(self):
        return f"Pessoa Jurídica ->  Razão Social: {self._razao_social} CNPJ:{self._documento} Cliente desde: {self.data_cadastro.strftime('%d/%m/%Y')}"
    
    def mostrar_cadastro(self):
        detalhes_cadastro = f"""
    Dados cadastrais
    ----------------
    Pessoa Jurídica
    Data cadastro:      {self.data_cadastro.strftime('%d/%m/%Y')}
    C.N.P.J.:           {self._documento}
    Razão Social:       {self._razao_social}
    Endereço:           {self._endereco.obter_completo()}
        """
        return detalhes_cadastro

    def cadastrar(self, cnpj = None):
        if (not cnpj):
            self._documento = input("CNPJ: ")
        self._razao_social = input("Informe a razão social: ")
        endereco = Endereco()
        endereco.cadastrar() 
        self._endereco = endereco