def fatorial(n):
    """função que retorna o fatorial de um número
    in=>int"""
    cont=1
    i=2
    while i<=n:
        cont = cont*i
        i+=1
    return cont