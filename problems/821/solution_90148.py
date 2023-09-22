def fatorial(num):
    """função que devolve o fatorial do num
    int->int"""
    n=num
    fat=1
    while n>0:
        fat=fat*n
        n=n-1
    return fat