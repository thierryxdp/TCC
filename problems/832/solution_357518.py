def eh_quadrada(A):
    """Dada uma matriz, essa função nos retorna True se ela for quadrada e False caso contrário; list -> bool"""
    
    if A == [] or len(A) == len(A[0]):
        return True
    else:
        return False