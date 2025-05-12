#Escreva um programa que leia números inteiros do teclado. O
#programa deve ler os números até que o usuário digite 0 (zero). No
#final da execução, exiba a quantidade de números digitados, assim
#como a soma e a média aritmética.

soma = 0
quantidade = 0
while True:
    num = int(input("Digite um numero inteiro: "))
    if num == 0:
        break
    soma = soma + num
    quantidade += 1
print("Quantidade de numeros digitados:",quantidade)
print("Soma =",soma)
print(f"Média = {(soma/quantidade):.2f}")