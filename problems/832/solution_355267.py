def eh_quadrada(A):
    '''retorna se a matriz é quadrada ou não'''
    if A == []:
        return True
    lin = len(A) 
    col = len(A[0]) 
    if lin == col:
        return True
    else: 
        return False