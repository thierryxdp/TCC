def eh_quadrada(matriz):
    """Procedimento que recebe uma matriz e confere, utilizando um dado booleando,
se ela é quadrada ou não.
assinatura: list --> bool
casos de teste:
eh_quadrada([[1,1,1], [1,1,1], [1,1,1]]) == True
eh_quadrada([[1,1,1], [2,2,2], [3,3,3]]) == True
"""
    if len(matriz) == 0 or len(matriz) == len(matriz[0]):
        return True
    else:
        return False