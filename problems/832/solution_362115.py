def eh_quadrada(mat):
    """Função que recebe uma matriz e retorna se ele é quadrada ou não.
    mat->bool
    """
    if mat == []:
        return True
    elif len(mat) == len(mat[0]):
        return True
    else:
        return False