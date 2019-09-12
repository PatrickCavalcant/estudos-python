def fatorial(n):
    fat = 1
    while(n>=1):
        fat = fat * n
        n = n - 1
    return fat
def fatorial_recursivo(n):
    if(n==1):
        return 1
    else:
        return n * fatorial_recursivo(n-1)
print(fatorial(4))
print (fatorial_recursivo(4))
