def fatorial(n):
    """funcao que dado um numero (n), calcula o fatorial deste numero. int->int"""
    proximo=0
    numero=range(1,n)
    
    while proximo<n:
        if proximo<n:
            n=n*numero[proximo]
        proximo= proximo+1
    return n