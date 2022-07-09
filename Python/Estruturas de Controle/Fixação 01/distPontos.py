x1 = float(input("Insira a primeira coordenada X: "))
x2 = float(input("Insira a segunda coordenada X: "))
y1 = float(input("Insira a primeira coordenada Y: "))
y2 = float(input("Insira a segunda coordenada Y: "))

D = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
D1 = D ** (1/2)

print(D1)
