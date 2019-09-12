x = int ( input (" Escreva a velocidade do carro "))

if x > 80:
    a = x - 80
    nv = a * 5
    print(" Sua multa é: R$ %d e a velocidade  passada é: %dKm" % (nv,a))
    
else :
    print("Não foi multado")
