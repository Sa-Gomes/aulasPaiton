print("Sistema de Cadastro")

nome = input("Nome: ")
senha = input("Senha: ")
opcao = input("Opção: ")
ListaPessoa = list()

if nome == "Samuel" and senha == "1406":
    print(f"Seja bem vindo {nome}")

else:
    print("Nome de Usuario ou senha incorretos")
    print("Para tentar novamente digite 01")
    print("Para cadastra-se digite 02")

if opcao == "01":
    if nome == "Samuel" and senha == "1406":
        print(f"Seja bem vindo {nome}")

