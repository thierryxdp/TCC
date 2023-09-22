def eh_quadrada(mt):
    """Função que recebe uma matriz e diz se ela 
    é quadrada ou não.
assinatura: list --> bool
casos de teste:
eh_quadrada([[2,1,3], [10,11,13], [71,12,17]]) == True
eh_quadrada([[0,0,0], [0,0,0], [0,0,0]]) == True
eh_quadrada([[0,0],[0,0]]) == True
"""
    if len(mt) == 0 or len(mt) == len(mt[0]):
        return True
    else:
        return False