def eh_quadrada(m):
    """ Dada uma matriz m, retorn True se ela for quadrada e
    False, caso contrário.
    list -> bool"""
    if m == [] and len(m) == len(m[0]):
        return True
    else:
        return False