def eh_quadrada(matriz):
    """retorna True se a matriz for quadrada e False se nao for
    list->bool"""
    if matriz == []:
        return True
    else:
        l=len(matriz)
        c=len(matriz[0])
        return l==c