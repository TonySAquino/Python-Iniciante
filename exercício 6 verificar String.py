#nesse exercicio iremos comparar duas Strings, ou seja, duas variaveis que não são compostas
#por números, e sim por caracteres (letras), como palavras por exemplo 
#lembrando que temos váriaveis do tipo int, que são variaveis numéricas com numeros inteiros
#e, portanto, não podem ser quebrados, temos variaveis do tipo float, que ai podemos ter
#numeros quebrados, como 5.5, e variaveis do tipo string, que são palavras. em outras linguagens
#de programação, comparar strings é um inferno, mas no Python é muito simples, por isso temos
#esse exercício

sexo = input("Digite F ou M para sexo da pessoa: ") #programa simples para definir o sexo 
                                                    #de alguém
if sexo == "F":
    print("O sexo é feminino")
elif sexo == "f":
    print("O sexo é feminino")
elif sexo == "M":
    print("O sexo é masculino")
elif sexo == "m":
    print("O sexo é masculino")
else:
    print("Caractere inválido")

#nesse programa, eu criei inclusive possibilidades para caso o usuário digite em minusculo, 
#visto que é muito intuitivo as pessoas digitarem em minusculo

#eu poderia escrever no lugar de sexo = input() o comando sexo = input().lower(), assim eu
#não precisaria de outros elifs para minusculos, o lower() inclui minusculos