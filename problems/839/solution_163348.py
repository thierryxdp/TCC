import math
def carros(p,v=5):
    '''função que calcula e retorna quantos carros são necessários
    para uma viagem, baseado na quantidade de pessoas; int, int->int'''
    return math.ceil(p/v)