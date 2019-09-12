contas = []
n_conta = 1

def p_nome():
    Nome = input("Digite o nome para ser titular: ");
    return Nome

def p_cpf():
    cpf = int(input("Digite o CPF do titular: "));
    return cpf

def novo():
     global contas, n_conta
     nome = p_nome()
     cpf = p_cpf()
     saldo = 0
     contas.append([nome, cpf, n_conta, saldo])
     n_conta = n_conta + 1
     
def depositar():
    pesquisar()
    Nome = input("Digite o valor valor a depositar");
    depositar = input(int("Digite o valor valor a depositar"));
    saldo = saldo + depositar
    e[4] = saldo
    
def sacar():
    Nome = input("O nome do usuario.");
    sacar = input(int("Digite o valor valor a sacar"));
    if saldo >= sacar:
        saldo = saldo - sacar
        
def mostrar():
    mostar = input("Digite o nome do titular")
    
def pesquisar():
    nome = p_nome()
    for p, e in enumerate(n_conta):
        if e[0].lower() == nome:
            return p
    return None





    


while True:
    print("""
   1 - Novo
   2 - Logar
   3 - Depositar
   4 - Sacar
   5 - Mostrar
   6 - Grava
   6 - Lê
   7 - Ordena por nome

   0 - Sai
""")
    opção = int(input("Digite a opção"))
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        print (contas)
    elif opção == 3:
        depositar()
    elif opção == 4:
        sacar()
    elif opção == 5:
        print (contas)








def altera():
     p = pesquisa(pede_nome())
     if p != None:
         nome = agenda[p][0]
         telefone = agenda[p][1]
         print("Encontrado:")
         mostra_dados(nome, telefone)
         nome = pede_nome()
         telefone = pede_telefone()
         agenda[p] = [nome, telefone]
