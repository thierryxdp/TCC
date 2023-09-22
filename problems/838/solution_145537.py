import math
def num_bombom(d,p):
    '''função que calcula quantos bombons Pedro consegue comprar, dados o dinheiro(d) e o preço do bombom(p) para realização da compra;
        int/float,int/float->int'''
    return math.floor(d/p)