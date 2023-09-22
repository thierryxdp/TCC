def eh_quadrada(matriz):
    # so lembrar que len(matriz) = linhas e len(matriz[0]) = coluna
    if len(matriz)==len(matriz[0]):
        return True
    elif len(matriz[0])==0:
        return True
    else:
        return False