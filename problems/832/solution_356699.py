def eh_quadradadef eh_quadrada(x):
    """ Retorna verdadeiro caso seja matriz. """
    matriz=[]
    if len(x) == len(x[0]):
        return True
    else:
        return False