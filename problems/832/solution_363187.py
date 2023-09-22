def eh_quadrada(matriz):
    ''''''
    if len(matriz)==0:
        return True
    for i in matriz:
        if len(matriz)==len(matriz[0]):
            return True
        else:
            return False