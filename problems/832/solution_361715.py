def eh_quadrada(matriz):
    ''''''
    linha1 = matriz[0]
    
    if linha1 in matriz:
        return False
    if linha1 not in matriz:
        return True