def eh_quadrada(mat):
    """Retorna verdadeiro se uma matriz for de ordem quadrada,
ou falso caso contrário. Obs.: uma matriz vazia é considerada quadrada.
assinatura:
mat --> bool
casos de teste:
eh_quadrada([[1, 1, 1], [2, 2, 2], [3, 3, 0]]) == True
eh_quadrada([[1, 1, 1], [2, 2, 2]]) == False
eh_quadrada([[1, 1], [2, 2]]) == True
eh_quadrada([]) == True
"""
    if mat == ([]):
        return True
    elif len(mat) == len(mat[0]):
        return True
    else:
        return False