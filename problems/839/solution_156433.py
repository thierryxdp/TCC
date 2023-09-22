import math
def carros(pessoas,c=5):
    '''a função deverá calcular o numero inteiro de carros
    baseando-se no numeros de pessoas,e no numero maximo de pessoas
    suportado em rodovias'''
    return math.ceil(pessoas/c)