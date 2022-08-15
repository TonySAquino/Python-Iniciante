#nesse exercicio, o objetivo é fazer o usuário inserir um valor, esse valor será salvo em uma variável, uma variável é uma palavra que eu digita, e nessa 
#palavra será salvo alguma informação, então no nosso comando que teremos, a palavra que eu quis usar é "numero", nessa palavra, alguma informação será salva
#nela, no caso a informação será o que o usuário digitar, graças ao comando float(input()), o float serve para informar que será um numero do tipo inteiro 
#que o usuario devera digitar para salvar nessa variavel numero, e o input() serve para que o programa reconheça o que o usuário digitar, e salve essa informação
#dentro da variável número.

#detalhe importante, dentro dos parenteses de input(), eu posso escrever algo entre aspas para aparecer na tela do usuário, nesse caso eu escrevi 
# "digite um número: " para que o usuário saiba o que ele deve digitar
numero = float(input("digite um número: "))

#pronto, agora temos o que o usuário digitou dentro da variavel número, vamos pedir para imprimir o que foi digitado no próximo comando de print, como já vimos
#na aula 1 de hello world

print(f"o numero digitado foi {numero}")

#o comando está diferente agora, certo? aqui vai uma explicação: dentro do que eu quero que imprima na tela do usuário, eu posso imprimir a variavel
#na tela, se eu escrever o nome dela entre chaves {}, no caso se eu escrever numero entre chaves, ficando {numero}, assim, o valor da variavel será impresso na 
#tela, mas para que eu consiga imprimir minhas variaveis juntas com a mensagem dentro do comando print, eu devo colocar um "f" antes das aspas, como foi feito,
#bem simples!


#nosso exercicio tem portanto apenas dois comandos, ficando 
#numero = float(input("digite um número: "))
#print(f"o numero digitado foi {numero}")