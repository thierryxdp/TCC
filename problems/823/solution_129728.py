def faltante (pecas):
    '''função que recebe uma lista de peças numeradas de 1 a N e retorna qual peça está faltando.
    list -> int'''
    
    indice = 1
    
    while indice in pecas:
        indice = indice + 1
    return indice