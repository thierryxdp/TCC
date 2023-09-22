def eh_quadrada(mt):
    '''Dado uma matriz, retorna se essa matriz é quadrada ou não.
    list -> bool'''
    if len(mt) == 0:
        return True
    elif len(mt) == len(mt[0]):
        return True
    else: 
        return False