def eh_quadrada(x):
    """ Retorna verdadeiro caso seja matriz. """
    if matriz == []:
        return True
    elif  len(matriz)== len(matriz[0]):
        return True
    else:
        return False