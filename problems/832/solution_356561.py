def eh_quadrada(x):
    """ Retorna verdadeiro caso seja matriz. """
    if len(x) == len(x[0]) or x ==[]:
        return True
    else:
        return False