import math

def carros(p,c=5):
    ''' Função que retorna o número exato de carros necessários para viajar, 
    dado ao número de pessoas(p) e
    a capacidade(c) caso os veículos tenham mais de 5 lugares ou menos.
    
    int, int(default==5) -> int'''
    return math.ceil(p/c)