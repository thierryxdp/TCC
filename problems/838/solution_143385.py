from math import floor
def num_bombons(V,P):
    '''calcula a quantidade de bombons que podem ser comprados
dado:
valor disponivel:V
preço:P'''
    return floor(V/P)