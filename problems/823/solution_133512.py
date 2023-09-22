def faltante(n):
    """Função que dada uma lista n -1 descubra qual a peça que está faltando; int-> int"""
    i=0
    while n[i]<len(n):
        if n[i+1]==n[i]:
            i=i+1
    return i+1