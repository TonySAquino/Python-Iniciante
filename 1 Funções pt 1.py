#o objetivo das funções é gerar um bloco de comandos separado do bloco principal, o bloco principal é basicamente o bloco
#que estavamos trabalhando dos exercicios 1 ao 8, ele é chamado de main, e é uma função.

#nesse bloco separadado, que será outra função, deixaremos códigos lá, para toda vez que precisarmos desses códigos, não
#precisarmos digitar eles toda hora, e sim só com um comando chamar eles que eles serão executados dentro da main naquela
#parte que ele foi chamado.

#muitos programadores irão me odiar pela minha definição, mas para um fácil entendimento, podemos sim comparar funções
#como variáveis que estamos mandando armazenar comandos dentro, em vez de só números e letras

#nosso comando pra chamar uma função será dado por def (), exemplo abaixo:

def batata():
    print('Hello ')
    print('Baby ')

#acima eu criei uma função com o nome de batata, e dentro dela tem dois prints, ou seja, dois comandos para imprimir algo 
#na tela do usuário. Quando eu chamar essa função acima no código abaixo, ela executará os comandos dentro dela

batata()