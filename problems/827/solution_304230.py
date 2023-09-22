def qtd_divisores(n):
    """ """
    div=1
    for div in range(n+1):
        div= range(n+1)//div
        div=div+1
    return div