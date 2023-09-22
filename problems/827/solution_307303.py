def qtd_divisores(n):
    """retorna o numero de divisores que n tem; int -> int"""
    p=1,2,3,5,7,11,13,17,19,23
    i=0
    for x in p:
        if n%x==0:
            i=i+1
    return i