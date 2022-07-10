sexo = str(input("Informe seu Sexo (F/M): "))
altura = float(input("Informe sua altura: "))

if sexo == "M":
    PI = (72.7 * altura) - 58
elif sexo == "F":
    PI = (62.1 * altura) - 44.7

print(PI)
