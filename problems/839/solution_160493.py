import math
def carros(p,c=5):
    ''' calcula o número exatos de carros necessários para uma viagem, dado o número de pessoas p e a capacidade máxima do carro c;
    	int,int->int'''
    return math.ceil(p/c)