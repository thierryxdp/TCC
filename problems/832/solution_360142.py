def eh_quadrada(matrizA):
    """..."""
    nlinhas=len(matrizA)
    nelementos=(matrizA[0])
    ncolunas=nelementos/nlinhas
    if nlinhas==ncolunas:
        return True
    else:
        return False