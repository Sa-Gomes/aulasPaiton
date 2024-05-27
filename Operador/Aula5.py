dia = input("Digite o dia da semana: ")
match dia:
    case "1":
        print("segunda")
    case "2":
        print("Terça")
    case "3":
        print("Quarta")
    case "4":
        print("Quinta")
    case "5":
        print("Sexta")
    case "6":
        print("Sábado")
    case "7":
        print("Domingo")

# Lista é filha vetor
pessoas = [
    ["Pedro", 31, "444.444.444.44", "11 9863 2587", "02145-581"],
    ["Maria", 28, "333.333.333.33", "11 96525 7740", "08472-510"],
    ["Tereza", 25, "222.222.222.22", "11 96645 8843", "82453-564"],
    # [None, None, None, None, None],
]
print(nomes[2] [1])

pesquisa = input("Digite o nome desejado: ").strip().title()

for linha in pessoas:


    if pesquisa == linha[0]:
        print(linha)