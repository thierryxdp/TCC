def eh_quadrada(m):
    """recebe uma matriz 'm' da forma lista de listas e retorna o valor booleano 'True' caso m seja quadrada e 'False' caso contrário;list->bool"""
    if m==[[]]:
        return True
    if len(m)==len(m[0]):
        return True
    else:
        return False