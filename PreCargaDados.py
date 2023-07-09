from datetime import datetime
from PessoaFisica import PessoaFisica
from Endereco import Endereco
from PessoaJuridica import PessoaJuridica


class PreCargaDados:
    
    def carga_dados(self):
        self.lista_clientes = []
        self.lista_contas = []
        print("Inicializando carga de dados...\n")
        self.carga_clientes_pessoa_fisica()
        self.carga_clientes_pessoa_juridica()
        print(f"Clientes cadastrados: {len(self.lista_clientes)}")
        print("Finalizando carga de dados...\n")

    def carga_clientes_pessoa_fisica(self):
        endereco = Endereco("Rua Honduras", "100", "Centro", "Santos", "SP")
        pessoa = PessoaFisica("1", "Horáicio Abukali", "01", "01", "1990", endereco)
        pessoa.data_cadastro = datetime(2001,10,2)
        pessoa.mostrar_cadastro()
        self.lista_clientes.append(pessoa)

        endereco = Endereco("Rua Sergine", "12", "Lajes Norte", "Ibirapuera", "SP")
        pessoa = PessoaFisica("2", "Mendes Soto", "01", "01", "1993", endereco)
        pessoa.data_cadastro = datetime(2021,1,3)
        pessoa.mostrar_cadastro()
        self.lista_clientes.append(pessoa)

    def carga_clientes_pessoa_juridica(self):
        endereco = Endereco("Rua Centro Sul", "99", "Colina Sul", "Monte Oeste", "RO")
        pessoa = PessoaJuridica("1001","Empreiteira SimelicoliNaste", endereco)
        pessoa.data_cadastro = datetime(2005,4,9)
        pessoa.mostrar_cadastro()
        self.lista_clientes.append(pessoa)

    def lista_clientes(self):
        return self.lista_clientes
    
    def lista_contas(self):
        return self.lista_contas
    

    