def eh_quadrada(matriz):
    if len(matriz)%2!=0 or len(matriz[0])!= len(matriz[-1]):
        return False
    else:
        return True