def faltante(lista):
    '''função em que dada uma lista com (N-1)inteiros, numerados de 1 a N, retorna qual
    número inteiro deste intervalo esta faltando; list->list'''
    pecas=0
    num=0
    encont=0
    som=(((1+(len(lista)+1))*(len(lista)+1))/2)
    list.sort(lista)
    while i<len(lista):
        if sum(lista) != som:
            num = (som)-sum(lista)
        pecas += 1
        encont += 1
    return num