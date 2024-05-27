nome = "Samuel"

valor1 = int(input("Digite a Nota"))

if valor1 <= 10:

    if valor1 >= 7 and valor1 <= 10:
        print("Aprovado")

    if valor1 >= 5 and valor1 <= 6:
        print("Exame")

    if valor1 <= 4:
        print("Reprovado")

else:
    print("Numero invalido")