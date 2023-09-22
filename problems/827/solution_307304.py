def qtd_divisores(n):
    """retorna o numero de divisores que n tem; int -> int"""
    a=list(range(n))
    i=0
    for x in a:
        if n%x==0:
            i=i+1
    return i