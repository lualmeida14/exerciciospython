#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
# 
nome = input ("Digite o seu nome")

altura = float(input("Digite sua altura"))

sexo = input("Você é (homem/mulher?)")

if (sexo == "homem"):
    altura = (72.7 * altura) -58
    print(f'Seu peso ideal é {altura:.2f} kg')

else:
    altura =(62.1* altura) - 44.7
    print(f'Seu peso ideal é {altura:.2f} kg')
