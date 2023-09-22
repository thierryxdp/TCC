def eh_quadrada(A):
    '''Função que recebe uma matriz e retorna True se ela for quadrada
    ou False caso contrário; list -> bool'''
    if A == [[]] or (len(A) == len(A[0])):
        return True
    else:
        return False