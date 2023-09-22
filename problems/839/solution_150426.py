from math import *
#Questão 1.2
def carros(p,c=5):
    '''calcula o número de carros de capacidade c necessário para transportar p pessoas'''
    return ceil(p/c)