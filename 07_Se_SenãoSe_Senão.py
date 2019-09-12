a = int(input("digite o primeiro valor"))
b = int(input("digite o segundo valor"))
op = input("digite o operador")

if op == "+":
    r = a + b
elif op == "-":
    r = a - b
elif op == "*":
    r = a * b 
elif op == "/":
    r = a / b
else:
    r = 0
print("resultado: %f" % r )
