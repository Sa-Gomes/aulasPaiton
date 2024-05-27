import os
import time
# def calMedia(n1:float, n2:float):
#     media = (n1 / n2)
#     return media
#
# print(calMedia(25,5))

# def somar(valor1, valor2):
#     return valor1 + valor2
#
# print(somar(20,10))

# def somar(n1, n2):
#     return n1 + n2
#
# valor1 = float(input("Digite primeiro numero: "))
# valor2 = float(input("Digite o segundo numero: "))
#
# print(somar(valor1, valor2))

import math
print("Calculadora")

def calcular(operacao:str, valor1:float, valor2:float):
    match operacao:
        case "+":
            return valor1 + valor2
        case "-":
            return valor1 - valor2
        case "*":
            return valor1 * valor2
        case "/":
            return valor1 / valor2
        case "**":
            return valor1 ** valor2
        case "sqrt":
            return valor1 ** valor2

while True:
    os.system("cls") or None

    print(f"Seja bem vindo a Calculadora")
    print("Operadores disponiveis")
    print("""
    + -> Soma
    - -> subtração
    / -> Divisão
    * -> Multiplicação
    ** -> Potência 
    sqr -> Raiz do Primeiro numero 
    """)

    operacao = input("Escolha uma operação: ")
    valor1 = float(input("Valor1: "))
    valor2 = float(input("Valor2: "))
    resultado = calcular(operacao, valor1, valor2)
    print("Você pediu para fazer a seguinte operação: ")
    print(f"Operação escolhida {operacao} | Resposta {resultado}")
    time.sleep(10)
    if operacao == "0":
        break



