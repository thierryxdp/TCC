def eh_quadrada(mat):
    """
"""
    linhas = len(mat)
    colunas = len(mat[0])
    if linhas == colunas:
        return True
    elif mat == []:
        return True
    else:
        return False