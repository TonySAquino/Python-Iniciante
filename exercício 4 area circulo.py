#nesse exercicio, deveremos calcular a area de um circulo. precisaremos do numero pi, para utiliza-lo no python, deveremos importar 
#uma biblioteca, bibliotecas são como códigos extras que podemos importar para usa-los, no caso da biblioteca math, traremos diversos
#comandos a mais que possibilitam operações matemáticas, incluindo o número pi

from math import pi #eu estou dizendo em from math import pi que, da biblioteca math, importar o número pi para meus códigos

raio = float(input("Por favor: informe o raio do circulo: "))
area = pi*(raio*raio)

print(f"A área do circulo é dada por {area}")