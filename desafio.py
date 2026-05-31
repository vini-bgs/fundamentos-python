#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = input("Olá! Qual o seu nome? ")

salario = int(input(f"Bem vindo, {nome}. Qual o valor do seu salário? "))

bonus = float(input("Qual o valor do bônus recebido? (Digite apenas o número do bônus. Ex: bônus de 15%, digite 15)"))

percent_bonus = (bonus / 100) + 1

calculo = 1000 + (salario * percent_bonus)

print(f"{nome}, o seu valor bônus foi de {calculo}")