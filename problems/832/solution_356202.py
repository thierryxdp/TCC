def eh_quadrada(matriz):
    """Função que retorna true para caso a matriz seja quadrada e false quando não for;
    list->bool"""
    if len(matriz) == [[]]:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False