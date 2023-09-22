def soma_h(n):
    """calcula e retorna H com N termos.
    int->float."""
    h=0
    for i in range(1,n+1):
        h=h+(1/i)
    return round(h,2)