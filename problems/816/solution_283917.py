def maiores(lInt,n):
    '''Retorna uma lista com todos os elementos da lista de
       de entrada maiores que o número n, também de entrada,
       ordenados em ordem crescente;
       list, int -> list'''
    lRetorno=[]
    for el in lInt:
        if el>n:
            lRetorno.append(el)
    lRetorno.sort()
    return lRetorno