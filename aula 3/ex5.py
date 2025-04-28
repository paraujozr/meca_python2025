#5. Escreva um programa que leia dois números e que pergunte qual
# operação você deseja realizar. Você deve poder calcular soma, subtração,
# multiplicação e divisão.
# Exiba o resultado da operação solicitada.


nuber1 = float(input("Digit o 1° numerous: "))
nuber2 = float(input("Digit o 2° numerous: "))
operacao = input("Digite qual operação vc quer realizar (+,-,* ou /) ")

if operacao == "+":
    resultado = nuber1 + nuber2
elif operacao == "-":
    resultado = nuber1 - nuber2
elif operacao =="*":
    resultado = nuber1
