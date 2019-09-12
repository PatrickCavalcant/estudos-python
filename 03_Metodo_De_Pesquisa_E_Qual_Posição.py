l = [5,7,3,20,55]
achou = False
pos = 0
p = int(input ("escreva o número a ser procurado: "))
for x in l:
    if (p == x):
        achou = True
        break
    pos += 1
if achou:
    print ("%d foi encontrado na posição %d" % (p,pos))
else:
    print ("%d não foi encontrado" % p)
