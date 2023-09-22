def insere(lista_numero,n):
    '''recebe uma lista e um numero inteiro e retorna uma lista ordenada
    list,int->list'''
    lista_numero= lista_numero +[n]
    lista_numero.sort()
    return lista_numero