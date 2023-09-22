def faltante (lista):
    """ dada uma lista de 1 a n sem repeticao, retorna o inteiro faltante na lista;
    list->int"""
    p=1
    lista.sort()
    while p<len(lista):
        if lista[p]-lista[p-1]>1:
           return lista[p]-1
        p=p+1
    if 1 in lista:
        return len(lista)+1
    else:
        return 1