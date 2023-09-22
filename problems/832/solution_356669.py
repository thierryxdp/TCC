def eh_quadrada(matriz):
    if len(matriz)==0 and len(matriz[0])==0:
        return True
    while len(matriz) > 0 and len(matriz[0]) > 0:
        if len(matriz)!=len(matriz[0]):
            return False
        elif len(matriz)==len(matriz[0]):
        return True