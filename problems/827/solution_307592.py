def qtd_divisores(n):
    """calcula quantos divisores o número n tem.
    int->int"""
    total=0
    for i in range(1,n+1):
        if n%i==0:
            total=total+1
    return total