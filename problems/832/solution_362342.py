def eh_quadrada(matriz):
    """Funcao que recebe uma matriz e retorna um valor booelano se ela for ou nao quadrada. list=>bool"""
    if len(matriz[0])==len(matriz):
        return True
    elif len(matriz)==0:
        return True
    else:
        return False