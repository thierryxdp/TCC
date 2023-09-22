def eh_quadrada(A):
    '''retorna se a matriz é quadrada ou não'''
    if A == [] or A == [[]]:
        return True
    lin = len(A) + 1
    col = len(A[0]) + 1
    elif lin == col:
        return True
    else: 
        return False