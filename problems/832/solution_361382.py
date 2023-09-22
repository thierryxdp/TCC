def eh_quadrada(m):
    '''dada uma matriz retorna se ela é quadrada ou nao
lista-> bool'''
    if len(m) == 0:
        return True
    elif len(m) == len(m[0]):
        return True
    else:
        return False