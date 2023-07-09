from datetime import datetime
from ContaCorrente import ContaCorrente
from PessoaFisica import PessoaFisica
from Endereco import Endereco
from PessoaJuridica import PessoaJuridica
from Deposito import Deposito
from Saque import Saque


class PreCargaDados:
    
    def carga_dados(self):
        self.lista_clientes = []
        self.lista_contas = []
        print("Inicializando carga de dados...\n")
        self.carga_clientes_pessoa_fisica()
        self.carga_clientes_pessoa_juridica()
        print(f"Clientes cadastrados: {len(self.lista_clientes)}\n")
        print(f"Contas cadastradas: {len(self.lista_contas)}\n")
        print("Finalizando carga de dados...\n")

    def carga_clientes_pessoa_fisica(self):
        enderecof1 = Endereco("Rua Honduras", "100", "Centro", "Santos", "SP")
        pessoaf1 = PessoaFisica("1", "Horáicio Abukali", "01", "01", "1990", enderecof1)
        pessoaf1.data_cadastro = datetime(2001,10,2)
        print(pessoaf1.mostrar_cadastro())
        self.lista_clientes.append(pessoaf1)

        conta_correntef1c1 = ContaCorrente.nova_conta(1, pessoaf1)
        conta_correntef1c1.mostrar_cadastro()        
        print(conta_correntef1c1.mostrar_cadastro())
        self.lista_contas.append(conta_correntef1c1)

        conta_correntef1c2 = ContaCorrente.nova_conta(2, pessoaf1)
        conta_correntef1c2.mostrar_cadastro()        
        print(conta_correntef1c2.mostrar_cadastro())
        self.lista_contas.append(conta_correntef1c2)

        enderecof2 = Endereco("Rua Sergine", "12", "Lajes Norte", "Ibirapuera", "SP")
        pessoaf2 = PessoaFisica("2", "Mendes Soto", "01", "01", "1993", enderecof2)
        pessoaf2.data_cadastro = datetime(2021,1,3)
        print(pessoaf2.mostrar_cadastro())
        self.lista_clientes.append(pessoaf2)

        conta_correntef2c1 = ContaCorrente.nova_conta(3, pessoaf2)
        conta_correntef2c1.mostrar_cadastro()        
        print(conta_correntef2c1.mostrar_cadastro())
        self.lista_contas.append(conta_correntef2c1)

    def carga_clientes_pessoa_juridica(self):
        enderecoj1 = Endereco("Rua Centro Sul", "99", "Colina Sul", "Monte Oeste", "RO")
        pessoaj1 = PessoaJuridica("1001","Empreiteira SimelicoliNaste", enderecoj1)
        pessoaj1.data_cadastro = datetime(2005,4,9)
        print(pessoaj1.mostrar_cadastro())
        self.lista_clientes.append(pessoaj1)

        conta_correntej1c1 = ContaCorrente.nova_conta(1001, pessoaj1)
        conta_correntej1c1.mostrar_cadastro()
        transacaoj1c1_1 = Deposito(100)
        pessoaj1.realizar_transacao(conta_correntej1c1, transacaoj1c1_1)
        transacaoj1c1_2 = Saque(3)
        pessoaj1.realizar_transacao(conta_correntej1c1, transacaoj1c1_2)
        print(conta_correntej1c1.mostrar_cadastro())
        print(conta_correntej1c1.saldo)
        print(len(conta_correntej1c1.historico.transacoes))
        conta_correntej1c1.listar_transacoes()
        self.lista_contas.append(conta_correntej1c1)

    def lista_clientes(self):
        return self.lista_clientes
    
    def lista_contas(self):
        return self.lista_contas
    

    