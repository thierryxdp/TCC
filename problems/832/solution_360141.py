def eh_quadrada(matrizA):
    """..."""
    nlinhas=len(matrizA)
    nelementos=len(matrizA[0])
    ncolunas=nelementos/nlinhas
    if matrizA==0:
        return True
    if nlinhas==ncolunas:
        return True
    else:
        return False