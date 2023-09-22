def eh_quadrada(mat):
    """Função que recebe uma matriz e retorna se ele é quadrada ou não.
    mat->bool
    """
    linhas = len(mat)
    colunas = len(mat[0])
    if linhas == colunas or linhas and colunas==0:
        return True
    else:
        return False