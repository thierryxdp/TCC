def faltante(n):
    """Função que dada uma lista n -1 descubra qual a peça que está faltando; int-> int"""
    n=n.sort()
    s=1
    while s==len(n):
        s=s+1
    return s