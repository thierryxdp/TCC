from math import *

#Questão 1.1
def num_bombons(d,p):
    '''calcula o número de bombons que Pedrinho consegue comprar com a quantidade de dinheiro d, com os bombons custando p'''
    return floor(d/p)