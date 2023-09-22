def qtd_divisores(n):
    """essa funcao, dado um numero n, calcula quantos divisores esse numero tem
    int -> int"""
    
    n_divisores = []
    
    for x in range (1, n+1):
        if n % x == 0:
            n_divisores += [x,]
    
    return len(n_divisores)