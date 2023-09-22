def qtd_divisores(n):
    """Funcao que conta quantos divisores o numero de entrada possui;
    int -> int"""
    
    divisores = 0
    for i in list(range(1,n+1):
        if n%i == 0:
            divisores += 1
        
    return divisores