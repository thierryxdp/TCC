import math
def carros(p,c=5):
    '''função que calcula e retornar o número exato de carros necessários para uma viagem, considerando que seja dado como entrada o número de pessoas(n) e a capacidade do veículo (c). Se não for dado a capacidade, a função interpretara que está indo em um veículo com capacidade de 5 pessoas'''
    return math.ceil(p/c)