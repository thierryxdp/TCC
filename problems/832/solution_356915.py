def eh_quadrada(m):
    """recebe uma matriz 'm' da forma lista de listas e retorna o valor booleano 'True' caso m seja quadrada e 'False' caso contrário;list->bool"""
    if (len(m)==0) or (len(m)==len(m[0]) and len(m)!=0):
        return True
    else:
        return False