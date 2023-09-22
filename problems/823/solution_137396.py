def faltante(lista):
    '''função que recebe uma lista com n-1 inteiros numerados de 1 a n e retorna qual elemento
    da lista está faltando
    lista -> int'''
    list.sort(lista)
    proximo = 0
    x = 1
    while proximo < len(lista) and x < len(lista):
        if lista[proximo] - lista[x] == -2:
            return lista[proximo] + 1
        proximo = proximo + 1
        x = x + 1
    if lista[0] == 2:
        return 1
    else:
        return lista[proximo] + 1