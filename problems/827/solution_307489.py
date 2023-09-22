def qtd_divisores(n):
    """calcula quantos divisores o número n tem.
    int->int"""
    total=0
    for i in range(n+1):
        if i!=0:
            if n%i==0:
                total=total+1
    return total