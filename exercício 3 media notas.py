#esse exercício já é mais complexo, utilizaremos o conceito de arrays.
#arrays são basicamente listas, e dentro dessa listas temos valores, por exemplo, uma lista com 5 notas escolares, sendo elas 6, 7, 8,  5, 6 formam um array
#para criar uma array, criamos uma variavel, nesse caso eu daria o nome de notas, e colocamos [], dentro desse [] eu coloco os valores que eu quero que
#fiquem armazenados como listas, comando será dado por

#notas = [6, 7, 8, 5, 6] 

#assim criei minha array com o nome de notas, mas para esse exercício, eu desejo que o usuário vá digitando os valores que sejam armazenados em notas, e 
#não que eu defini antes, como sendo 6, 7, 8, 5 e 6, para isso, meu código ficará da seguinte forma:
print("digite 10 notas para calcular a média: ")#estou orientando o que o usuário deve digitar com esse print para contextualizar ele
notas = [float(input()) for i in range(0, 10)]

#o que está sendo dito nesse código? teremos uma array com o nome de notas, já que estaremos usando a estrutura notas = [], e dentro de [], teremos um float(input()),
#indicando que trabalharemos com numeros inteiros que o usuário digitar, portanto tudo que o usuário digitar, em forma de números inteiros, será armazenado como um
#elemento da lista, ou array, de nome notas, e temos ainda algo novo: for i in range(0,10), aqui eu estou falando basicamente o seguinte: quando eu tenho range(0, 10),
#significa que eu vou ter uma lista que vai do elemento de numero zero, que é nosso primeiro elemento dentro da lista, até o elemento de número 9, que é o decimo elemento
#da lista, ou seja, será uma lista com 10 elementos, 10 notas; em python, o primeiro elemento é sempre o número zero, e graças ao for i, nós iremos passar de elemento em
#elemento até o último elemento definido em range, o i portanto irá iniciar no elemento de numero 0 de posição, portanto o primeiro, e depois irá para o segundo, e assim vai
#até o décimo elemento, eu sei que é confuso isso explicado de forma digitada, mas de maneira geral, float(input() for i in range(0, 10)) significa que o que o usuário
#digitar será salvo em 10 elementos que irão compor um array, conforme ele vai dando enter, vai indo pro proximo elemento, até chegar no décimo; se fosse 
#float(input() for i in range(0, 5)), tudo que o usuário fosse digitando e dando enter seria até 5 elementos para uma array, bem simples o comando na prática.
#por que eu peguei 10? porque esse exercício quer que eu calcule a média de 10 notas de um aluno, então com esse comando, o usuário digitará 10 valores, cada um pra um
#elemento, que irá representar uma nota, e todos esses elementos irão compor uma lista, ou array, com o nome de notas

print(notas)
#com esse comando, será impresso na tela do usuário a lista que ele formou com as notas que ele digitou

#vamos então somar o que o usuário digitou para dividir por 10 e assim podermos calcular essa média:
soma = sum(notas)#esse comando irá somar, através de sum, todos os elementos dentro da array notas, desde que eu a escreva nos parenteses, e armazenar numa variável nova que
                 #eu chamei de soma
media = soma/10
print(f"A média é {media}")

notas = float(input() for i in range(0, 10))