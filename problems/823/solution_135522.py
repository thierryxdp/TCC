def faltante(lista):
    '''Dado uma lista de números inteiros de 1 a n, 
    retorna o numero faltante entre eles; list -> int'''
    list.sort(lista)
    i=0
    lista2=list(range(len(lista)+1))[1:]
    if lista2 == lista:
        return lista[-1]+1
    while lista2[i] == lista[i]:
        i=i+1
    if lista2[i] != lista[i]:
        return lista2[i]