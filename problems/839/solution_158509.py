"""
Nesta função iremos informar o número de pessoas para a viagem e dividir este
valor pelo número de assentos em cada veículo, com a possibilidade de informar
números de assentos fora do padrão. Usamos a função math.ceil para transformar
o valor quebrado dado pela divisão e transformá-lo em um valor inteiro, já
que não podemos ter um veículo fracionado. É necessário importar o módulo math
para podermos utilizar esta solução.
int, int -> int
"""
import math
def carros(pessoas,assentos=5):
    x = pessoas/assentos
    return math.ceil(x)