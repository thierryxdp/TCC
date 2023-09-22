def eh_quadrada(matriz):
    # so lembrar que len(matriz) = linhas e len(matriz[0]) = coluna
    if len(matriz)==0:
        return True
    elif len(matriz)!=len(matriz[0]):
        return False
    else:
        return True