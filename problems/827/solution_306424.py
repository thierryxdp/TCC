def qtd_divisores(n):
    """Funcao que conte quantos divisores um número tem.
    int -> int"""
    divisivel=0
    for x in range (1,n+1):
        if n % x == 0:
            divisivel+=1
    return divisivel