def eh_quadrada(lista):
    '''A função retorna, dada uma matriz, se ela é quadrada ou não
    list -> bool'''
    if lista == []:
        return True
    elif len(lista) == len(lista[0]):
        return True
    else:
        return False