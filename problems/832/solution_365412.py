def eh_quadrada(matriz):
    indice=(len(matriz))
    while indice>=0:
        if matriz[indice]==matriz[indice-1]:
            return True
        else:
            return False
        indice=indice-1