#Esse arquivo servirá apenas para eu testar códigos, ignorem isso C=
from time import sleep

def salve(a, b):
    c = a+b
    print(c)

resposta = float(input('Digite 1 para sim, 2 para não: '))
if resposta == 1:
    sleep(1)
    a = float(input('Informe o primeiro numero: '))
    sleep(1)
    b = float(input('Informe o segundo numero: '))
    salve(a, b)

else:
    sleep(1)
    print('Obrigado por participar do código')