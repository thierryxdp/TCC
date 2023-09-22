def eh_quadrada(lista:list)->bool:
    """ A função identifica se uma matriz é quadrada ou não, e
    retorna True se ela for quadrada, e False se não for"""
    if lista == [] or len(lista) == len(lista[0]):
        return True
    else:
        return False