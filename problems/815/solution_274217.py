def insere(lista_numero,n):
    '''insere um numero de forma que ele mantenha a ordem
    ascendente
    list,int->list'''
    a=lista_numero+[n]
    a.sort()
    return a