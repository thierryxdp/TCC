def eh_quadrada(lista:list)->bool:
    """ A função identifica se uma matriz é quadrada ou não, e
    retorna True se ela for quadrada, e False se não for"""
    if len(lista) == len(lista[0]) or len(lista) == 0:
        return True
    else:
        return False