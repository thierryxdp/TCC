def eh_quadrada(matriz):
    ''''dada uma matriz, diz se ela é quadrada ou não
    matriz de inteiros -> bool'''    
    if len(matriz) == len(matriz[0]):
        return True
    elif len(matriz) == 1 and len(matriz[0]) == 0:
        return True
    elif len(matriz) != len(matriz[0]):
        return False
    elif sum(matriz) == 0:
        return True