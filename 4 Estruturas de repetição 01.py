#A ideia de estruturas de repetição é que a gente crie blocos, e dentro desses blocos
#os comandos nele fiquem se repetindo, caso  uma  condição  que  tenhamos determinado
#ainda não tenha sido atingida. Exemplo abaixo:

n = 5
while n<10:
    print(n)
    n = n+1

#basicamente, eu defini que n será 5 na linha 5, na linha 6, com o comando while, eu
#disse que, enquanto ("while" significa "enquanto") a variavel n  for menor  que  10
#(eu disse isso com n<10), os comandos identados logo abaixo deverão se repetir,  no
#caso os comandos são print(n), que vai mandar imprimir  a variavel,  e  em  seguida 
#n = n + 1, que vai atualizar o valor de n, ou seja, n agora vai ser n anterior mais 1,
#então no primeiro ciclo de repetição, n = 5, n valor novo de n será 5+1 que será igual 
#a 6, esse valor continua menor que 10, então a repetição irá acontecer, ele irá imprimir
#novamente o valor de n, que agora será 6, e em n = n +1 teremos que n = 6 + 1 = 7,
#e assim ele vai até atingir o 10