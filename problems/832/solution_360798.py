def eh_quadrada(matriz):
    "recebe uma matriz e verifica se esta é quadrada"
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False