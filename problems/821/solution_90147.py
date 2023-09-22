def fatorial(n):
    """
    Função recebe um número n e calcula o fatorial deste número.
    int -> int
    """
    if n==1:
        return 1
    else:
    	valor=n*(n-1)
    	n-=2
    while n>0:
        valor*=n
        n-=1
    return valor