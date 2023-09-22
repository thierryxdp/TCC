import math
def num_bombons(d,p):
    ''' calcula quantos bombons conseguem ser comprados, dados o dinheiro d e o preço p do bombom;
    	int/float,int/float->int '''
    return math.floor(d/p)