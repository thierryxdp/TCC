def faltante(numeros):
    """funçao faltante que dada uma lista com N-1 inteiros numerados de 1 a N descubra qual interiro esta faltando 
    list ->int""""
    
    a = max(numeros)
    b = math.factorial(a)
    c = sum(numeros)
    d =b-c
    return d