def faltante(lista):
    ''' função que dada uma lista N-1 inteiros,numerados de 1 a N,descobre qual numero inteiro deste intervalo esta faltando; list->int'''
    list.sort(lista)
    j = 0
    n = 1
    while j<len(lista):
        if lista[j] == j+1:
            n = lista[j] + 1
        j += 1
    return n