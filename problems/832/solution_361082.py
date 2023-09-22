def eh_quadrada(matriz):
    'dada uma matriz, identifique se é uma matriz quadrada. list(list)-->bool'
    if len(matriz)== len(matriz[0]):
        return True 
    else:
        False