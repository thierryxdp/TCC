def faltante(LP):
    '''função que retorna a peça faltante de um quebra-cabeças
    dado uma lista de peças(LP) numeradas de 1 a N.
    list-->int'''
    LP.sort()
    i=0
    while i<len(LP):
        if LP[1] != i+1:
            return i+1
        i=i+1
    return  LP[-1]+1