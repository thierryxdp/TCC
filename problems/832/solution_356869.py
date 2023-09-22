def eh_quadrada(matriz):
    """Identifica se a matriz é quadrada.
    Parametros:
    Entrada:list
    Saida:Boolena"""
    if matriz==[]:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False