def qtd_divisores(n):
    """Funcao que conta quantos divisores o numero de entrada tem;
    Entrada: int
    Sainda: int"""
    
    div=0
    for i in range(n+1):
        if n%i == 0:
            div+=1
    return div