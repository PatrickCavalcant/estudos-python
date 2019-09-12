lista = [1,2,3]
n = int(input("digite se quer  1 adicionar ou outro valor para retirar: "))
if n == 1:
    ad = input ("digite o valor a adicionar: ")
    lista . append(ad)
    print (lista)
else :
    re = int(input ("digite o valor a retirar: "))
    del lista[re] 
    print (lista)
