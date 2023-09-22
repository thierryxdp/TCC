def qtd_divisores(n):
    """
    retorna o numero de divisores que n possui
    """
    total=0
    for i in range(1,n+1):
        if n//i==n/i:
            total+=1
    return total