def fatorial(n):
    """Função que calcula a fatorial de um número"""
    """int--->int"""
    i=1
    resposta=1
    while i<n:
        resposta*=i
    return resposta