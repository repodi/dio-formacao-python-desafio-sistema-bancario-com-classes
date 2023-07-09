class Endereco:         
    def __init__(self, logradouro = None, numero = None, bairro = None, cidade = None, uf = None):
        self._logradouro = logradouro
        self._numero = numero
        self._bairro = bairro
        self._cidade = cidade 
        self._uf = uf

    def __str__(self):
        return self.obter_completo()
    
    def obter_completo(self): 
        endereco =  f"{self._logradouro}"
        if (self._numero):
            endereco += f", {self._numero}"
        if (self._bairro):
            endereco += f" - {self._bairro}"
        if (self._cidade):
            endereco += f" - {self._cidade}"
        if (self._uf):
            endereco += f" - {self._uf}"
        return endereco
    
    def obter_rua(self): 
        endereco =  f"{self._logradouro}"
        if (self._numero):
            endereco += f", {self._numero}"
        return endereco
    
    def cadastrar(self):
        print("Cadastro do endereço:...")
        self._logradouro = input("Logradouro: ")
        self._numero = input("Número: ")
        self._bairro = input("Bairro: ")
        self._cidade = input("Cidade: ")
        self._uf = input("UF: ")