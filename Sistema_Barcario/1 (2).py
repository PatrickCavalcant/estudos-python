class Cliente:
    def __init__(self,nome,cpf):
        self.__nome = nome 
        sefl.__cpf = cpf
    def getnome():
        return self.__nome
    def getcpf():
        return self.__cpf
class Conta:
    def __init__ (self,cliente,numero,saldo=0):
        self.__cliente=cliente
        self.__numero=numero
        self.__saldo=saldo
    def sacar(self,valor):
        self.__saldo -= valor
    def deposita(self,deposita):
        self.__saldo+=valor
    def versaldo(self):
        return self.__saldo
    
class contaespecial(Conta):
    def __init__(self,cliente,numero,saldo=0,limite=0):
        Conta.__init__(self,cliente,numero,saldo)
        self.__limite=limite

Conta=Conta ("a",1,100)
print(Conta)
  
        

