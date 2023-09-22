def qtd_divisores(n):
    """Retorna quantos divisores o número n tem.
    int->int"""
    divisores=0
    for num in range(n+1):
        if n%num==0:
            divisores=divisores+1
    return divisores