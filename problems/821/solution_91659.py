def fatorial (n):
    """Retorna o fatorial da entrada n; int->int"""
    i=n
    cont = 1
    while i!=1:
		cont = cont *i
        i = i - 1
    return cont