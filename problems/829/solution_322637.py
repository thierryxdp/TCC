def soma_h(n):
    """calcula e retorna H com N termos.
    int->float."""
    h=0
    for i in range(n):
        h=h+(1/n)
    return round(h,2)