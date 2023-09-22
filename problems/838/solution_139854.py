def num_bombons(d,p):
    '''função que, dado o dinheiro que Pedrinho possúi, d, e o preço de um bombom, p, calcula a quantidade máxima de bombons que podem ser comprados.
    float, float --> int'''
    return round((d/p)+0.5)