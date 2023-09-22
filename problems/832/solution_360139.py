def eh_quadrada(matrizA):
    """..."""
    nlinhas=len(matrizA[0])
    nelementos=len(matrizA[0])
    ncolunas=nelementos/nlinhas
    if nlinhas==ncolunas:
        return True
    else:
        return False