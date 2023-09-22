from math import floor

def num_bombons(d,p):
    '''Calcula e retorna quantos bombons Pedrinho poderá comprar dados d = dinheiro
    que Pedrinho tem e p = preço unitário do bombom.
    Só aceita valores positivos para d e p.
    float, float -> int'''
    return floor(d/p)