def qtd_divisores(n):
    """ """
    div=1
    for div in range(n+1):
        if n%div==0:
            return  div
    div=div+1
    
    return div