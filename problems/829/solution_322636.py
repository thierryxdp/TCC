def soma_h(n):
    """calcula e retorna H com N termos.
    int->float."""
    h=1
    for i in range(n+1):
        h=h+(1/n)
    return round(h,2)