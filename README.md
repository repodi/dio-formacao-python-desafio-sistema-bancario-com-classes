# Sistema bancário em Python

Desafio DIO da Formação Python Developer que tem por objetivo a construção de um sistema bancário utilizando classes na linguagem Python.

## Objetivo

Criar um sistema bancário com as operações: sacar, depositar, visualizar extrato, cadastrar usuário(cliente) e cadastrar conta bancária. 
Armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários.  

## Narrativa do escopo 

O banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
As operações de saque, depósito e extrato somente estarão disponíveis para usuários cadastradas e após informar sua agência e conta.
Para realizar operações primeiro o usuário deve ser cadastrado após o seu cadastro será criada uma conta para o usuário. 

### cadastrar usuário
O usuário deve ser cadastrado no sistema. 
A identificação do usuário é o número do seu CPF. Este número deve ser único, não permitindo o cadastro de um CPF mais de uma vez.  
Para cadastro do usuário serão informados os seguintes campos: 
- cpf
- nome 
- data de nascimento
- endereço

O endereço será composto das seguintes informações: 
- logradouro
- número
- bairro
- cidade / sigla do estado

### criar conta corrente

As contas correntes são armazenadas em uma lista. 
Para o cadastro da conta corrente serão informados os seguintes campos: 
- agência
- número da conta 
- usuário 

O usuário pode ter mais de uma conta cadastrada.
O número da agéncia é fixo "0001".

### Operação de depósito

Deve ser possível depositar valores positivos para a conta bancária. 
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato. 

### Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. 
No fim da listam deve ser exibido o saldo atual da conta. 
Se o extrato estiver em branco, exibir a mensagem: 

*Não foram realizadas movimentações*

## Instruções
 
- Para iniciar o sistema executar a classe SistemaBancario.py
- A classe PreCargaDados.py irá realizar uma carga inicial de dado, remover as refêrencias a esta classe para que o sistema inicialize sem nenhum dado pré cadastrado. 

## Diagrama do modelo conceitual 

Para a construção do sistema bancário seguir a construção do modelo definido em UML. 
![Modelo UML](/diagrama-modelo-uml.png)




