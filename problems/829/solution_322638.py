def soma_h(n):
    """calcula e retorna H com N termos.
    int->float."""
    h=0
    for i in range(n+1):
        if i!=0:
            h=h+(1/i)
    return round(h,2)