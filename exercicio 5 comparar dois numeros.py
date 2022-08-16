#esse exercicio servirá para que o usuário digite dois números, e assim seja impresso na tela dele o maior.
#o objetivo desse exercício é vermos as estruturas condicionais, no caso if

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

#como iremos comparar os dois números para pedirmos para o maior ser impresso? através do if:
if numero1>numero2:                         #aqui eu estou dizendo que SE o número1 for maior que o número 2, o que 
    print(f"O maior é {numero1}")           #está com uma tabulação abaixo deverá ser executado. no caso é um print

elif numero2>numero1: #aqui eu estou dizendo que, se if anterior não for satisfeito, eu terei um outro if, que será 
    print(f"O maior é {numero2}") #escrito elif, diminutivo de else if,e que se satisfeito, o que está com uma 
                                  #tabulação abaixo deverá ser executado,outro print

else: #aqui eu estou dizendo que, se nenhuma das condições dos if anteriores forem satisfeitas, afinal é isso que 
    print(f"Os números são iguais")#significa o ELSE (SE NÃO), o que está com uma tabulação abaixo deverá ser executado,
                                   #que também é um print

#estrutura if else é muito simples, basicamente temos que if condição: , que significa SE a seguinte condição for 
#feita, execute as linhas de baixo, e temos o else: que significa SE NÃO for satisfeita, execute essas linhas de baixo
