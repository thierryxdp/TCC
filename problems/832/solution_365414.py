def eh_quadrada(matriz):
    indice=(len(matriz))-1
   
    while indice>=0:
        if matriz[indice]==matriz[indice-1] and len(matriz)==matriz[indice]:
            return True
        indice=indice-1
    return False