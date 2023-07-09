from ContaCorrente import ContaCorrente
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica
from PreCargaDados import PreCargaDados
from Deposito import Deposito
from Saque import Saque

SENHA_MANUTENCAO = "1234"


lista_clientes = []
lista_contas = []
numero_ultima_conta = 0

def busca_cliente_por_documento(documento):
    global lista_clientes
    for cliente in lista_clientes: 
        if cliente.documento == documento:
            return cliente
    else: 
        return None
    
def buscar_conta(cliente, agencia, nro_conta):    
    global lista_contas
    for conta in lista_contas: 
        if cliente.documento == conta.cliente.documento and agencia == conta.agencia and int(nro_conta) == conta.numero:
            return conta
    else: 
        return None
    
def acessar_conta():
    documento = input("Informe o cpf ou cnpj para acessar suas contas:")
    cliente_existente = busca_cliente_por_documento(documento) 
    if cliente_existente: 
        agencia = input("Informe sua agência: ")
        nro_conta = input("Informe o número da sua conta corrente: ")
        conta_existente = buscar_conta(cliente_existente, agencia, nro_conta)
        if conta_existente:
            acessar_menu_conta(documento, agencia, nro_conta)
        else:
            print("A conta não existe!")
    else:
        print("Cliente não cadastrado!")

def extrato(cliente, agencia, nro_conta): 
    conta = buscar_conta(cliente, agencia, nro_conta)
    print("\n================ EXTRATO ================")
    if not conta.historico:
        print("Não foram realizadas movimentações.")
    else: 
        conta.listar_transacoes()
    print(f"\nSaldo: R$ {conta.saldo:.2f}")
    print("==========================================")

def depositar(cliente, agencia, nro_conta):    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = buscar_conta(cliente, agencia, nro_conta)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def sacar(cliente, agencia, nro_conta):
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = buscar_conta(cliente, agencia, nro_conta)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def cadastrar_conta():
    global numero_ultima_conta
    global lista_clientes
    global lista_contas
    documento = input(f"Informe o CPF ou CNPJ do cliente: ")
    cliente = busca_cliente_por_documento(documento) 
    if not cliente:
        print("CPF ou CNPJ do cliente não esta cadastrado, cadastre o cliente primeiro")
        return None
    else:
        numero_ultima_conta = numero_ultima_conta + 1
        nova_conta = ContaCorrente.nova_conta(numero_ultima_conta, cliente)
        lista_contas.append(nova_conta)
        print("Nova conta cadastrada...\n")
        print(nova_conta)

menu_conta = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

def acessar_menu_conta(documento, agencia, nro_conta):
    cliente = busca_cliente_por_documento(documento)
    print(f"Bem vindo !")
    print(cliente)
    while True: 
        opcao_menu_conta = input(menu_conta)
        if opcao_menu_conta == "d":
            depositar(cliente, agencia, nro_conta)
        elif opcao_menu_conta == "s": 
            sacar(cliente, agencia, nro_conta)
        elif opcao_menu_conta == "e": 
            extrato(cliente, agencia, nro_conta)
        elif opcao_menu_conta == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

menu_tipo_cliente = """

[f] Cadastrar PessoaFísica
[j] Cadastrar Pessoa Jurídica

=> """

def cadastrar_usuario():
    print("Cadastrando novo cliente ---> ")
    tipo_pessoa = input(menu_tipo_cliente)
    cliente = None
    if (not tipo_pessoa == "f" and not tipo_pessoa == "j" ):
        print("Opção inválida!")        
    elif (tipo_pessoa == "j"):
        cliente = PessoaJuridica()
        cliente.cadastrar()
    else:
        cliente = PessoaFisica()
        cliente.cadastrar()
    lista_clientes.append(cliente)    
    print(f"Cliente  cadastrado")
    print(cliente.mostrar_cadastro())

def listar_clientes(cpf=None):
    global lista_clientes
    print(f"Quantidade clientes cadastrados: {len(lista_clientes)} \n") 
    print("Lista de clientes:\n")
    for cliente in lista_clientes: 
        print(cliente)

def listar_contas():
    global lista_contas
    documento = input(f"Informe o CPF ou CNPJ para um cliente em especifico ou pressione enter para todos clientes: ")
    if documento:
        cliente = busca_cliente_por_documento(documento)
        if not cliente:
            print("CPF do cliente não esta cadastrado")
            return None
    print("Lista de contas:\n")
    for conta in lista_contas:
        if documento :
            if conta.cliente.documento == documento:
                print(conta)
        else: 
            print(conta)
            

menu_manutencao = """

[u] Cadastrar Usuário (Cliente)
[l] Listar clientes
[c] Nova Conta
[o] Listar contas
[q] Sair

=> """

def acesso_manutencao():
    senha = input("Informe a senha de manutenção:")
    senha = "1234"
    if (senha == SENHA_MANUTENCAO):        
        while True: 
            opcao_manutencao = input(menu_manutencao)
            if opcao_manutencao == "u":
                cadastrar_usuario()
            elif opcao_manutencao == "l":
                listar_clientes()
            elif opcao_manutencao == "c":
                cadastrar_conta()
            elif opcao_manutencao == "o":
                listar_contas()
            elif opcao_manutencao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
    else: 
        print("Senha de manutenção inválida.")

menu_geral = """

[a] Acessar conta
[m] Manutenção
[l] Desligar sistema

=> """

print("Inicializando sistema...\n")
pre_carga = PreCargaDados()
pre_carga.carga_dados()
lista_clientes = pre_carga.lista_clientes
lista_contas = pre_carga.lista_contas
numero_ultima_conta = 5000

while True: 
    opcao = input(menu_geral)
    if opcao == "m":
        acesso_manutencao()
    elif opcao == "a": 
        acessar_conta()
    elif opcao == "l":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")