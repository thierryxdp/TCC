def faltante(lista):
    '''Dado uma lista de números inteiros de 1 a n, retorna o numero que falta entre eles. list -> int'''
    list.sort(lista)
    i=0
    listaf=list(range(len(lista)+1))[1:]
    if listaf == lista:
        return lista[-1]+1
    while listaf[i] == lista[i]:
        i=i+1
    if listaf[i] != lista[i]:
        return listaf[i]