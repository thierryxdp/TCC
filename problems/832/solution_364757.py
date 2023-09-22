def eh_quadrada(mtz):
    """Procedimento que recebe uma matriz e confere se ela é quadrada ou não.
assinatura: list --> bool
casos de teste:
eh_quadrada([[3,3,3], [2,2,2], [1,1,1]]) == True
eh_quadrada([[4,4,4], [2,2,2], [6,6,6]]) == True
"""
    if len(mtz) == 0 or len(mtz) == len(mtz[0]):
        return True
    else:
        return False