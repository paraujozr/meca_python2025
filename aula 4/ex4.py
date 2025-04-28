'''4. Faça um programa para imprimir de 1 até o número
digitado pelo usuário que mostre apenas os números
ímpares.'''


x = 1
jose = int(input("Digite um numero: "))
while x <= jose:
    if x % 2 != 0:
        print(x)
    x += 1

