def eh_quadrada(A):
    '''
    	A função recebe uma matriz e retorna True se ela for quadrada e False caso
        contrário. Obs: uma matriz vazia é considerada quadrada.
        A -> list (matriz)
        list -> Bool
    '''
    if A == []:
        return True
    elif len(A[0]) == len(A):
        return True
    else:
        return False