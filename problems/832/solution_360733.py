def eh_quadrada(matriz):
    """Função que identifica se uma matriz é quadrada ou não
    entrada: list
    saída: bool"""
    if len(matriz)==0 and len(matriz[0])==0:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False