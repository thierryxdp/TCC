def soma_h(n):
    """
    Retorna o valor de H.
    int -> float
    """
    h=0
    for i in range(1,n+1):
        h += 1/i
    return round(h,2)