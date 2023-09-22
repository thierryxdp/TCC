def eh_quadrada(x):
    """ Retorna verdadeiro caso seja matriz. """
    if x==[]:
        return True
    elif len(x) == len(x[0]):
        return True
    else:
        return False