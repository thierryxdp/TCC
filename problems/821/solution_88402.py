def fatorial(n):
    """funcao que recebe um numero(n) e retorna o valor do fatorial deste numero.
    entrada->int
    saida->int"""
    i=1
    j=1
    while i< n:
        j=j*(i+1)
        i=i+1
    return j