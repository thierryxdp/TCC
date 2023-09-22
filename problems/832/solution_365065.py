def eh_quadrada(A):
    '''
    Recebe uma matriz e verifica se a mesma é quadrada ou não.
    Se for quadrada retorna o boleano True e não sendo quadrada retorna o boleano False
    '''
    
    if not A:  
        return True  
    m = len(A)  
    n = len(A[0])  
    if m == n:  
        return True  
    else:  
        return False