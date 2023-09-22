def eh_quadrada(matriz):
    for i in range(len(matriz)):
        if len(matriz[i])==len(matriz):
            return True
        elif len(matriz)==0:
            return True
        else:
            return False