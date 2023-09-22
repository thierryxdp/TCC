def eh_quadrada(lista):
    ''' identifica se uma matriz é quadrada, list->boleano'''
    if len(lista)==0:
            return True
    for i in lista:
        if len(i)==len(lista):
            return True
        else:
            return False