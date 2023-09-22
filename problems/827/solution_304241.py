def qtd_divisores(n):
    """ """
    qtd_div=1
    for div in range(2,n):
        if n % div ==0:
            qtd_div = qtd_div+1
    
    return qtd_div + 1