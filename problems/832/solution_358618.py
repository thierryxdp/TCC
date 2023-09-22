def eh_quadrada(matriz):
    """Função que retorna True se uma matriz é quadrada e false
    caso contrário; list->bool"""
    if matriz==[]:
        return True
    nlin=len(matriz)
    ncol=len(matriz[0])
    if ncol!=nlin:
        return False
    else:
        return True