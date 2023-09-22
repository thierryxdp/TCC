import math

def quant_carros(p,c=5):
    '''retorna a quantidade de carros com capacidade de transporte c necessária para uma viagem com p pessoas'''
    '''int,int->int'''
    if(type(p)!=int)or(type(c)!=int):
        return 'p e c devem ser números inteiros'
    elif(p<0)or(c<0):
        return 'p e c devem ser números positivos'
    else:
        return math.ceil(p//c)