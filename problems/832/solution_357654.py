def eh_quadrada(matriz):
    tamanhoMatriz=len(matriz)
    tamanhoElementos=len(matriz[0])
    if len(matriz)==0:
        return True
    elif tamanhoMatriz==tamanhoElementos:
            return True
    else:
        return False