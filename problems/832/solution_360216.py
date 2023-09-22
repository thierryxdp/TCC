def eh_quadrada(lista):
    '''Verifica se a matriz enviada é quadrada
    list---->bool'''
    if len(lista)==0:
        return True
    elif len(lista) == len(lista[0]):
        return True
    else:
        return False