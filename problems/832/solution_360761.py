def eh_quadrada(matriz):
    "dada uma matriz, retorna booleano se a mesma for quadrada"
    if matriz == []:
        return len(matriz) == 0
    return len(matriz) == len(matriz[0])