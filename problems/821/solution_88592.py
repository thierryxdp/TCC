def fatorial(n):
    """funcao que dado um numero (n), calcula o fatorial deste numero. int->int"""
    proximo=1
    numero=n
    while proximo<numero:
        if proximo<numero:
            n=proximo*n
        proximo= proximo+1
    return n