#Nesse programa, iremos perguntar ao usuários 5 perguntas sobre um crime. se ele responder
#duas positivamente, será suspeito, se responder 3 a 4, será cúmplice, e se responder 5 
#será classificado como assassino. Caso seja menos de duas, será inocente

from tkinter import Y


soma = 0

print("Responda as perguntas a seguir, seguindo essas instruções: ")
print("Digite 'S' para sim, 'N' para não, digite apenas a letra, nada a mais")
print("Digite todas as letras uma abaixo da outra, cada linha respondida será a da pergunta correspondente")

print("Telefonou para a vitima? \n Esteve no local do crime?\nMora perto da vitima?")
print("Devia para a vitima?\nJá trabalhou com a vitima?")

respostas = [input() for i in range(0, 5)]

i = 0

while i < 5:
    if respostas[i] == "S":
        soma = soma + 1
    i = i+1

if soma < 2:
    print("Inocente")
elif soma == 2:
    print("Suspeito")
elif soma >2|soma<5: #a barra em pé significa "e", ou seja, se a soma for maior que dois e menor que 4:
    print("Cumplice")
elif soma==5:
    print("Culpado!")