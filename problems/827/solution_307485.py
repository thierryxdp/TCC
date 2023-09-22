def qtd_divisores(n):
    """calcula quantos divisores o número n tem.
    int->int"""
    total=0
    for i in range(n):
        if n%i==0:
            total=total+1
    return total