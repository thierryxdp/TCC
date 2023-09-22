def qtd_divisores(n):
    """llkfdjsklfnsdk"""
    
    n_divisores = 0
    
    for x in range (1, n+1):
        if n % x == 0:
            n_divisores += 1
    return n_divisores