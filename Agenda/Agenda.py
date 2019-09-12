lista = []
I=0
arquivo = open("agenda.txt","w")

while True:
    
    print("____________________________")
    print("           AGENDA           ")
    print("____________________________")
    print("       1. Adicionar         ")
    print("       2. Alterar           ")
    print("       3. Excluir           ")
    print("       4. Visualizar        ")
    print("       5. Sair              ")
    print("                            ")
    n = int(input("Digite a opção desejada? "))
    print("_____________________________")

    if n == 1:
        ad = input("Digite o Nome: ")
        numero = input("Digite o Número: ")
        lista.append ( "Nome: " + ad + " Número:" + numero)
        
        
    elif n==2:
        print(lista)
        at = int(input("Digite a posição do número a alterar: "))
        A = input("Digite o novo nome: ")
        B = input("Digite o novo número: ")
        lista[at] = ("Nome: " + A + " Número: " + B)
        
    elif n== 3:
        print(lista)
        re = int(input("Digite a posição do número a ser retirar: "))
        del lista[re]
        
    elif n==4:
        print(lista)
            
    elif n == 5:
        break
    
    else:
        print("VALOR INVALIDO")
   
for linha in lista:
    arquivo.write("%s\n" % linha )
    
arquivo.close()

    


