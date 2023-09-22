def qtd_divisores(n):
    """int -> int"""
    """retorna quantos divisores n tem"""
    
    d = 0
    
    for i in range(1,n+1):
        if n%i == 0:
            d += 1
            pass
        pass
    return d