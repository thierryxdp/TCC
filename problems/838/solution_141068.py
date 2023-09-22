import math
def num_bombons(d, p):
    '''calcula quantos bombons poderão serio comprados, considerando "d" o 
    dinheiro disponível e "p" o preço dos bombons'''
    return math.ceil(d/p)