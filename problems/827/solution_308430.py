def qtd_divisores(n):
    """conta quantos divisores um dado numero inteiro n tem
    int --> int"""
    qtd_d=0
    for i in range(1,n+1):
        if n%i==0:
            qtd_d=qtd_d+1
    return qtd_d