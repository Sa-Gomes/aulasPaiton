# import datetime as dt
# print("Sistema".center(__width = 50, __fillchar = "#"))
#
# pessoas = list()
#
# while True:
#     print("""
#         1 - Cadastrar
#         2 - Buscar
#         3 - Deletar
#         4 - Listar
#         5 - Sair
#     """)
#
# Menu = input("Digite uma opção: ").strip()
# if menu in ["1","2","3","4","5"]:
#     match menu:
#         case "1":
#             print("Cadastrar".center(__width= 50, __fillchar= "#"))
#             nome = input("Digite o nome: ").strip().title()
#             ano_nasc + input()
#
#
#         case "2":
#             print("Buscar".center(__width = 50, __fillchar = "#"))
#             busca = input("Digite o nome que deseja buscar: ").strip().title()
#             for linha in pessoas:
#                 if busca == linha[0]:
#                     print(f"Nome: {linha[0]}")
#                     print(f"Idade: {anoAtual - int(linha[1])}")
#                     print(f"Senha {linha[2]}")
#
#         case "3":
#             print("Deletar".center(__width = 50, __fillchar = "#"))
#             op_deletar =input("Qual pessoa deseja deletar: ").strip().title()
#             for indice, linha in enumerate(pessoas):
#                 if op_deletar == linha[0]:
#                     pessoas.remove(linha)
#             print("Deletado com sucesso!")
#         case "4":
#             print("Listar Pessoas".center(__width = 50, __fillchar = "#"))
#             for indice, linha in enumerate(pessoas):
#                 print(f"{indice} - {linha}")
#
#         case "5":
#             break
#
#
# else:
#     print("Essa opção não existe")
