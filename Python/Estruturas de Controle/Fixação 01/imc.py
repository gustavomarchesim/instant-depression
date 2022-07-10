peso = float(input("Insira o seu peso em KGs: "))
altura =  float(input("Insira sua altura em metros: "))

imc = peso / altura**2

if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print("Você tem o peso normal!")
elif imc >= 25 and imc < 30:
    print("Você está acima do peso!")
elif imc > 30:
    print("Você está obeso!")