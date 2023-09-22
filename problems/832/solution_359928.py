def eh_quadrada(matriz):
    """função que verifica se a matriz recebida é quadrada.
    list -> bool"""
    if len(matriz) == 0 or len(matriz) == len(matriz[0]):
        return True
    else:
        return False