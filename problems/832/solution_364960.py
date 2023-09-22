def eh_quadrada(matriz):
    """funcao booleana que identifica se uma matriz e quadrada ou nao
list->bool"""
    for j in range(0,len(matriz)):
        if len(matriz[j]) == len(matriz):
            return True
    if matriz == []:
            return True
    else:
            return False