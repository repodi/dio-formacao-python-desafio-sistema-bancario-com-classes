from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica
from PreCargaDados import PreCargaDados

SENHA_MANUTENCAO = "1234"
LIMITE_SAQUES = 3
AGENCIA = "0001"
limite = 500

lista_clientes = []
lista_contas = []
numero_ultima_conta = 0

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
                continue
            elif opcao_manutencao == "c":
                #cadastrar_conta()
                continue
            elif opcao_manutencao == "o":
                #listar_contas()
                continue
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


while True: 
    opcao = input(menu_geral)
    if opcao == "m":
        acesso_manutencao()
    elif opcao == "a": 
        #acessar_conta()
        continue
    elif opcao == "l":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")