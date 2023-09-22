def qtd_divisores(n):
    """retorna quantos divisores o numero n possui;
    int -> int"""
    d=()
    for x in range(1,n+1):
        if n%x==0:
            d=d+x
    return len(d)