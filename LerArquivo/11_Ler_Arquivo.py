arquivo = open("11_Arquivo.txt","r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
