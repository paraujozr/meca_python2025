nuber1 = float(input("Digit o 1° numerous: "))
nuber2 = float(input("Digit o 2° numerous: "))
operacao = input("Digite qual operação vc quer realizar (+,-,* ou /) ")

if operacao == "+":
    resultado = nuber1 + nuber2
elif operacao == "-":
    resultado = nuber1 - nuber2
elif operacao == "*":
    resultado = nuber1 * nuber2
elif operacao == "/":
    resultado = nuber1 / nuber2
else:
    print("Operação nada a ver com o bonde!")
    resultado = 0
print("Resultado: ", resultado)

