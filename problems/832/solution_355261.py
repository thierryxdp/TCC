def eh_quadrada(A):
    '''retorna se a matriz é quadrada ou não'''
    lin = len(A) + 1
    col = len(A[0]) + 1
    if lin == col:
        return True
    else: 
        return False