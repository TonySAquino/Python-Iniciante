#exemplo de função abaixo. Para ficar de fácil entendimento, comece a ler o código a partir da linha 9, onde a main começa, 
#a função que eu criei com o nome de slave nas linhas 7 a 9 iremos ver depois

from time import sleep #estou chamando um comando sleep da biblioteca time, esse comando faz o programa dormir por tantos
                       #segundos, eu devo informar. exemplo: sleep(1)   isso fará o programa dormir por 1 segundo, apenas
                       #estou usando isso para não ser imprimido tudo de uma vez na tela
def salve(g, h): #repare que as duas variaveis que eu mandei trazer, aqui na função em si eu nomeei diferente, isso 
    c = g+h      #acontece porque eu na verdade crio novas variaveis que receberão, na mesma ordem, os valores de variaveis
    print(c)     #daquelas que eu enviei, tanto que eu poderia usar a e b também, não teria problema

resposta = float(input('Digite 1 para sim, 2 para não: '))
if resposta == 1:
    sleep(1)
    a = float(input('Informe o primeiro numero: '))
    sleep(1)
    b = float(input('Informe o segundo numero: '))
    salve(a, b) #repare que dessa vez eu estou enviando as variaveis a e b para a função dentro dos parenteses

else:
    sleep(1)
    print('Obrigado por participar do código')

    #agora leia a função nas linhas 7 a 9