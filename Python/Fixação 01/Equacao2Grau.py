A = float(input("Insira o primeiro número: "))
B = float(input("Insira o segundo número: "))
C = float(input("Insira o terceiro número: "))

D = B**2 - 4*A*C

if A == 0:
    print("O valor de A, deve ser diferente de 0")
elif D < 0:
    print("Sem raízes reais")
else:
    x1 = (-B + D ** (1 / 2)) / (2 * A)
    x2 = (-B - D ** (1 / 2)) / (2 * A)
    
    print("x1: {}, x2: {}".format(x1, x2))