def eh_quadrada(A):
    '''retorna se a matriz é quadrada ou não'''
    lin = len(A)
    col = len(A[0])
    if lin == col:
        return True
    else:
        return False