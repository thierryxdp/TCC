import math
def carros(pessoas,capacidade=5):
    ''' função que calcula e retorna a quantidade de carros necesários (int)
    para uma certa quantidade de pessoas(int) para uma viagem, tendo em vista
    a capacidade de cada carro(int), considerando que se não for especificado a
    a capacidade é de 5 pessoas por carro'''
    	return math.ceil(pessoas/capacidade)