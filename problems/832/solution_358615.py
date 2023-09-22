def eh_quadrada(matriz):
    """Função que retorna True se uma matriz é quadrada e false
    caso contrário; list->bool"""
    nlin=len(matriz)
    ncol=len(matriz[0])
    if matriz==[]:
        return True
    elif ncol!=nlin:
        return False
    else:
        return True