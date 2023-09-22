def eh_quadrada(matriz):
    """dada uma matriz em forma de lista, na qual cada elemento
    seja uma lista, que representa as linhas dessa matriz e cada
    int dessas linhas seja elemento de uma coluna, retorna se a matriz
    é quadrada, ou seja, se ela possui o mesmo numero de linhas e colunas
    list --> bool"""
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False