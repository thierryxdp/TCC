def qtd_divisores(n):
    """conta quantos divisores um numero tem
    int -> int"""
    d=0
    for t in range(1,n+1):
        if n%t==0:
            d+=1
    return d