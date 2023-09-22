def filtraMultiplos(lista, num):
    '''lista que recebe um alista e num número e devolve
    uma nova lista cujos valores são aqueles números da lista
    que são múltiplos do número dado'''
    lista_div = []
    for i in lista:
        if i%num == 0:
            lista_div.append(i)
    return lista_div