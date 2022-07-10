cod = int(input("Informe o código do produto desejado: "))

if cod == 1:
    print("Alimento não perecivél")
elif cod in range(2, 5):
    print("Alimento perecivél")
elif cod in range(5, 7):
    print("Vestuário")
elif cod == 7:
    print("Higiene Pessoal")
elif cod in range(8, 16):
    print("Limpeza e utensilios domésticos")
else:
    print("Inválido")
