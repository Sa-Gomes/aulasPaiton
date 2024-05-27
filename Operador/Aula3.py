#nome = (nome da pessoa)
nome = "carlos"
nome2 = "Maria"
nome4 = "Pedro"

#print(nome)
print(nome[-6])
print(nome[1:4])
print(nome[2:])
print(nome[:5])
print(nome[2:-2])
print(nome[::-1])

#loop ou laço de repetição
for letra in nome:
    print(letra)

listaNomes = ["Carlos","Maria","Pedro"]

for nome in listaNomes:
    print(nome)

pessoa = ["Carlos",38,5.000,"masculino"]

for index in [0,1,2,3]:
    print(pessoa[index])

for index in range(4):
    print(pessoa[index])

for valor in range(1,9):
    print(valor)

for valor in range(10,0,-1):
    print(valor)

for valor in range(0,21,2):
    print(valor)

#tabuada
for valor in range(0,11):
    print(f"2 x {valor} = {valor * 2}")

for valor1 in range(0,11):
    for valor in range(0, 11):
        print(f"{valor1} x {valor} = {valor * valor1}")
    print(" ")





