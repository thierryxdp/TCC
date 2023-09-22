def qtd_divisores(n):
    """ """
    divisor = 0
    for divisor <len(n):
        if n%divisor==0:
            divisor = divisor +1
    return len (divisor)