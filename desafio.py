#Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.




while True:
    try:
        nome = input("Olá! Qual o seu nome? ").strip()

        for l in nome:
            if not l.isalpha() and l != " ":
                raise ValueError(f"Você digitou um caractere não válido >> {l} \n"
                                "Digite novamente...")
        break

    except ValueError as err:
        print(f"Atenção! {err}")

while True:
    try:
        salario = input(f"Bem vindo, {nome}. Qual o valor do seu salário? ")

        for n in salario:
            if n == ",":
                raise ValueError("Utilize '.' ao invés de ',' como separador decimal")
            elif not n.isnumeric() and n != ".":
                raise ValueError(f"Você digitou um caractere não válido >. {n}\n"
                                    "Digite novamente...")
            
        salario = float(salario)
        break
    except ValueError as err:
        print(f"Atenção! {err}")

while True:
    try:
        bonus = input("Qual o valor do bônus recebido? (Digite apenas o número do bônus. Ex: bônus de 15%, digite 15)")

        for b in bonus:
            if n == ",":
                raise ValueError("Utilize '.' ao invés de ',' como separador decimal")
            elif not b.isnumeric() and b != ".":
                raise ValueError(f"Você digitou '{b}' incorretamente. Utilize apenas números: ")
            
        bonus = float(bonus)
        break
    except ValueError as err:
        print(f"Atenção! {err}")

percent_bonus = (bonus / 100) + 1

calculo = 1000 + (salario * percent_bonus)

print(f"{nome}, o seu valor bônus foi de R${calculo}.")